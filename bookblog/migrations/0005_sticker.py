# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookblog', '0004_auto_20171124_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker_title', models.CharField(max_length=200)),
                ('sticker_image', models.ImageField(upload_to='images/stickers')),
            ],
        ),
    ]
