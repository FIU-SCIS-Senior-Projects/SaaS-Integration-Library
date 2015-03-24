import os


def populate():
    trello_api = add_api(name="trello", calls={'get_all_boards', 'get_all_cards', 'get_members', 'get_lists', 'get_labels'})

    trello_cred = add_api_cred(name="Trello Test",
                 settings={'key': '36fb61b8a99b93c4cbf0b63a5f440503',
                           'token': '36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe'},
                 api=trello_api)

    add_call(api_obj=trello_api, call_name="get_all_boards")


def add_api(name, calls):
    p = Api.objects.get_or_create(name=name, calls=calls)[0]
    return p

def add_api_cred(name, settings, api):
    p = ApiCredential.objects.get_or_create(name=name, settings=settings, api=api)[0]
    return p

def add_call(api_obj, call_name):
    p = Call.objects.get_or_create(api=api_obj, name=call_name)[0]
    return p

if __name__ == '__main__':
    print "Starting SIL population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SaaS_Integration_Library.settings')
    import django
    django.setup()
    from SIL.models import Api, ApiCredential, Call

    populate()
