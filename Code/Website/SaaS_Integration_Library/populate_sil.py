import os
import pprint


def populate():
    add_api_cred(name="Trello Test",
                 settings={'key': '36fb61b8a99b93c4cbf0b63a5f440503',
                           'token': '36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe'})


def add_api_cred(name, settings):
    p = Api_Credential.objects.get_or_create(name=name, settings=settings)[0]
    return p


if __name__ == '__main__':
    print "Starting SIL population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SaaS_Integration_Library.settings')
    from SIL.models import Api_Credential

    populate()
