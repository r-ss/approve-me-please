# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permalink', models.SlugField(max_length=10, verbose_name='Permalink')),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('filetype', models.CharField(max_length=4, verbose_name='Filetype')),
                ('filename', models.CharField(max_length=16, verbose_name='Filename')),
                ('file_size', models.FloatField(verbose_name='File Size')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
        ),
    ]
