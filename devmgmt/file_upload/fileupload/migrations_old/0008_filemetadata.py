# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0007_auto_20170710_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileMetaData',
            fields=[
                ('file', models.FileField(upload_to=b'')),
                ('file_type', models.CharField(default=b'N/A', max_length=10)),
                ('link', models.CharField(max_length=500, primary_key=True, serialize=False)),
            ],
        ),
    ]
