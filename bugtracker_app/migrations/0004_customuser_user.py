# Generated by Django 3.1.7 on 2021-02-24 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0003_auto_20210223_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]