# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0023_auto_20170812_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ekfile',
            old_name='file',
            new_name='file_upload',
        ),
    ]

