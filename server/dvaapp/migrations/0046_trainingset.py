# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0045_auto_20171222_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_task_type', models.CharField(choices=[('D', 'Detection'), ('I', 'Indexing'), ('C', 'Classication')], db_index=True, default='D', max_length=1)),
                ('instance_type', models.CharField(choices=[('I', 'images'), ('V', 'videos')], db_index=True, default='I', max_length=1)),
                ('count', models.IntegerField(null=True)),
                ('name', models.CharField(default='', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
            ],
        ),
    ]