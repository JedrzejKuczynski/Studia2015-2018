# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171129_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
