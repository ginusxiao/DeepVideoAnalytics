# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0016_auto_20170829_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retriever',
            old_name='source_filter',
            new_name='source_filters',
        ),
        migrations.RemoveField(
            model_name='indexerquery',
            name='excluded_index_entries_pk',
        ),
        migrations.RemoveField(
            model_name='indexerquery',
            name='source_filters',
        ),
    ]
