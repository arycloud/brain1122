# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-12 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20171010_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggedarticle',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]
