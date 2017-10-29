# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 05:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171029_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.FileField(default='', upload_to='images/', verbose_name='File'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL),
        ),
    ]
