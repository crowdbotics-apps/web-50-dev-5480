# Generated by Django 2.2.13 on 2020-06-05 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
        ('users', '0002_auto_20200605_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bbfjghgfjhgf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bbfjghgfjhgf', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='user',
            name='cvcvcvc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nbvnbvnbv',
            field=models.ManyToManyField(blank=True, related_name='user_nbvnbvnbv', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='user',
            name='ujgjhgjhg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ujgjhgjhg', to=settings.AUTH_USER_MODEL),
        ),
    ]
