# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-13 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='Topic',
            new_name='topic',
        ),
    ]