import json

from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .predict import prepare_data, predict
from .serializers import Prediction, PredictionSerializer
from .models import BankStatement
from .serializers import UserSerializer, BankStatementSerializer


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class BankStatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankStatement.objects.all()
    serializer_class = BankStatementSerializer


class PredictAPIView(APIView):

    def get(self, request, pk):
        weeks = request.GET.get('weeks') or 1
        data = BankStatement.objects.get(user_id=pk).data
        pred = predict(prepare_data(json.dumps(data)), int(weeks))
        prediction = Prediction(weeks=weeks, **pred)
        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)
