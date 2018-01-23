# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ('-result',)},
        ),
        migrations.RemoveField(
            model_name='operation',
            name='op',
        ),
        migrations.AddField(
            model_name='operation',
            name='operation',
            field=models.CharField(blank=True, choices=[('SUM', '+'), ('SUB', '-'), ('MUL', '*'), ('DIV', '/'), ('POW', '^')], max_length=1),
        ),
        migrations.AddField(
            model_name='operation',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='operation',
            name='result',
            field=models.FloatField(editable=False, null=True),
        ),
    ]