# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations

def load_data(apps, schema_editor):
    ApiCred = apps.get_model("SIL", "ApiCredential")
    Api = apps.get_model("SIL", "Api")
    Call = apps.get_model("SIL", "Call")
    
    ApiCred(name="Trello Test",
        settings={'key': '36fb61b8a99b93c4cbf0b63a5f440503',
        'token': '36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe'},
        ).save()

    Api(credentials=ApiCred.objects.all()[0],
        name="trello",
        calls={'get_all_boards', 'get_all_cards', 'get_members', 'get_lists', 'get_labels'},
        ).save()

    Call(api=Api.objects.all()[0],
         name='get_all_boards',
        ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('SIL', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
