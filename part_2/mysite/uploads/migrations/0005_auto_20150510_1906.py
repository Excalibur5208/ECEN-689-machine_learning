# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='title',
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to=b'cars'),
        ),
    ]
