# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imghost', '0002_image_date_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='date_edited',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
