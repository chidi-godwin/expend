from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import BankStatement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class BankStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankStatement
        fields = ['id', 'user', 'data']


class Prediction:
    def __init__(self, weeks: int, dates: list, predicted_amounts: list):
        self.weeks = weeks
        self.dates = dates
        self.predicted_amounts = predicted_amounts


class PredictionSerializer(serializers.Serializer):
    weeks = serializers.IntegerField()
    dates = serializers.ListField()
    predicted_amounts = serializers.ListField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass