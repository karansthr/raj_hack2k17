# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_evidence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Evidence',
        ),
    ]
