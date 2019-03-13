# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-20 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles_app', '0002_auto_20180420_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]