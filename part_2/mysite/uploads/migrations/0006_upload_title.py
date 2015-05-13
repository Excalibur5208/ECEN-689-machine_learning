# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20150510_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
