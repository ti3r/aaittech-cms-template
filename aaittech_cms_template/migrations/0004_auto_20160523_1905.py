# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('aaittech_cms_template', '0003_auto_20160519_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='aapersonaldisplay',
            name='image_new',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='aaportfolioitemshow',
            name='image_new',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image'),
        ),
    ]
