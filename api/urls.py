from django.urls import path
from .views import UserList, BankStatementDetail, PredictAPIView


urlpatterns = [
    path('users/', UserList.as_view()),
    path('statements/<int:pk>/', BankStatementDetail.as_view()),
    path('predict/<int:pk>/', PredictAPIView.as_view()),
]
