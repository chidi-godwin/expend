from django.contrib import admin
from .models import User, BankStatement

# Register your models here.
admin.site.register(User)
admin.site.register(BankStatement)
