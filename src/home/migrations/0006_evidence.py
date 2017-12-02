# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_evidence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.FileField(blank=True, upload_to=home.models.image_upload_location)),
            ],
        ),
    ]
