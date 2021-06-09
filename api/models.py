from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f"User: {self.username}"


class BankStatement(models.Model):
    id = models.OneToOneField(User, models.CASCADE, related_name="bank_statement", primary_key=True)
    data = models.JSONField()

    def __str__(self):
        return f"Bank Statement: {self.user.username}"
