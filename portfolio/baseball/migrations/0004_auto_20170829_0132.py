# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-29 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0003_auto_20170820_0227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ret_code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('aka', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
    ]