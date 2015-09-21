# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imghost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_event',
            field=models.DateTimeField(null=True),
        ),
    ]
