# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('signage', '0003_sign_use_frameset')]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='status',
            field=models.CharField(choices=[('auto', 'Auto - Schedule/Eighth'), ('autourl', 'Auto - URL/Eighth'), ('eighth', 'Eighth Period'), (
                'schedule', 'Bell Schedule'), ('status', 'Schedule/Clock'), ('url', 'Custom URL')], default='auto', max_length=10),),
    ]
