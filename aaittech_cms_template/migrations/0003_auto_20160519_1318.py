# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaittech_cms_template', '0002_aapersonaldisplay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aapersonaldisplay',
            name='image_height',
            field=models.IntegerField(default=120),
        ),
    ]
