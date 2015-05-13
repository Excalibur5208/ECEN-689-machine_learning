# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_remove_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='file',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
