# Generated by Django 3.2.3 on 2021-06-09 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankstatement',
            name='user',
        ),
        migrations.AlterField(
            model_name='bankstatement',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='bank_statement', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]