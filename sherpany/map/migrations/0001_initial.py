# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitude')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longitude')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
            ],
        ),
    ]