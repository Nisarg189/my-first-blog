# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171106_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvoteCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvoteCount',
            field=models.IntegerField(default=0),
        ),
    ]
