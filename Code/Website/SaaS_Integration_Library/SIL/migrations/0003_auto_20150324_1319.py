# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SIL', '0002_load_trello_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='api',
            name='credentials',
        ),
        migrations.AddField(
            model_name='apicredential',
            name='api',
            field=models.ForeignKey(default='test', to='SIL.Api'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(default=b'trello', max_length=128),
            preserve_default=True,
        ),
    ]
