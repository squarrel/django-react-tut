# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]