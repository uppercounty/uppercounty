# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150525_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=25)),
                ('bio', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('image_file', models.ImageField(blank=True, upload_to='coach-images')),
            ],
            options={
                'verbose_name_plural': 'coaches',
            },
        ),
    ]
