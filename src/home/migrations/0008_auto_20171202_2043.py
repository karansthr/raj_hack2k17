# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20171202_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='evidence',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='evidence',
            name='doc',
            field=models.FileField(blank=True, upload_to=home.models.doc_upload_location),
        ),
        migrations.AddField(
            model_name='evidence',
            name='image2',
            field=models.ImageField(blank=True, upload_to=home.models.image_upload_location),
        ),
        migrations.AddField(
            model_name='evidence',
            name='video',
            field=models.FileField(blank=True, upload_to=home.models.doc_upload_location),
        ),
    ]
