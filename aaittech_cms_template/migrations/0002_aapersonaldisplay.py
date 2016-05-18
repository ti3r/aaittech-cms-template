# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaittech_cms_template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AAPersonalDisplay',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(upload_to=b'')),
                ('image_width', models.IntegerField(default=100)),
                ('image_height', models.IntegerField(default=100)),
                ('image_alt', models.CharField(default=b'', max_length=50)),
                ('p_name', models.CharField(default=b'', max_length=100)),
                ('p_title', models.CharField(default=b'', max_length=250)),
                ('p_about', models.CharField(default=b'', max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
