# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160303_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=b'', blank=True),
        ),
    ]