from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

import simplejson

import sys
sys.path.append("/home/adam/")
from senior import secret
import datetime

from apis import trello
from SIL.models import ApiCredential, Api, Call


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('SIL/index.html', context_dict, context)

def datasource(request):
    context = RequestContext(request)
    context_dict = {'trello_key' : secret.TRELLO_KEY}

    return render_to_response('SIL/datasource.html', context_dict, context)

def confirmation(request, api_name):
    context = RequestContext(request)
    context_dict = {'api_name' : api_name}
    token = request.GET.get('token', '')

    #TODO Trello hardcoded!
    #make request to get email, use to add to api name, i.e. allowing multiple emails for given api
    trello_obj = trello.Trello(token)
    user_name = trello_obj.get_records()['username']
    context_dict['username'] = user_name

    api = Api.objects.get(name=api_name.lower())
    credentials = ApiCredential.objects.create(name=(api_name+' '+user_name), settings={'key': secret.TRELLO_KEY,'token': token}, api=api)

    return render_to_response('SIL/confirmation.html', context_dict, context)

def datasets(request):
    context = RequestContext(request)

    context_dict = {}

    #TODO have global list of current api names
    api_list = ['trello']

    try:
        cred = {}
        for api_name in api_list:
            cur_api = Api.objects.get(name=api_name)
            api_creds = ApiCredential.objects.filter(api=cur_api)
            for api_cred in api_creds:
                cred[api_cred.name] = api_cred.name.replace(' ', '_')

        context_dict['datasets'] = cred

    except AttributeError:
       pass

    return render_to_response('SIL/datasets.html', context_dict, context)

def api(request, api_cred):
    context = RequestContext(request)

    context_dict = {'api_cred': api_cred}

    try:
        cred = ApiCredential.objects.get(name=api_cred.replace('_', ' '))
        api = cred.api
        context_dict['api'] = api

        #loop through calls to clear out '_'s between names
        context_dict['calls'] = {}
        for call in api.calls:
            context_dict['calls'][call] = call.replace('_', ' ')

        context_dict['credentials'] = cred.settings['token']

    except Api.DoesNotExist:
        pass

    return render_to_response('SIL/api.html', context_dict, context)


def apicall(request, api_cred, action_name):
    context = RequestContext(request)

    action = action_name.replace('_', ' ')          #name to display
    cred = ApiCredential.objects.get(name=api_cred.replace('_', ' '))

    user_name = api_cred.split('_')[1]

    context_dict = {'action_name': action_name}

    try:
        #need if to check whether api credentials exist already?
        #Get the Api object, then obtain the credentials from the given Api and create object to make calls
        api = cred.api
        api_tok = cred.settings['token']

        #make more modular, name lookup
        api_obj = trello.Trello(api_tok)
        api_obj.set_username(user_name)

        #delete it to make more recent call
        Call.objects.filter(name=action_name).delete()

        #what about if call requires argument?
        #create call object to as to return
        call = Call.objects.create(api=api,name=action_name, response=getattr(api_obj, action_name)())
        context_dict['call'] = call
        context_dict['response'] = call.response
        context_dict['action'] = action.upper()
        context_dict['card_lists'] = {}
        context_dict['card_lists']['mycards'] = api_obj.get_cards_assigned_to_me()
        context_dict['assigned_count'] = len(context_dict['card_lists']['mycards'])
        context_dict['total_cards'] = api_obj.get_total_cards()
        context_dict['card_lists']['past_due_cards'] = api_obj.cards_past_due
        context_dict['past_due_count'] = len(context_dict['card_lists']['past_due_cards'])
        context_dict['card_lists']['due_cards'] = api_obj.due_in_seven
        context_dict['due_in_seven_count'] = len(context_dict['card_lists']['due_cards'])


        items = []
        for item in call.response:
            #TODO find http and make link, then append
            items.append(item)

        context_dict['card_lists']['total'] = items

        labels = []
        for k,v in call.response[0].iteritems():
            labels.append(k)

        context_dict['labels'] = labels
        context_dict['items'] = items

        if action_name == 'get_all_cards':
            date = datetime.datetime.now()
            context_dict['year'] = date.year
            context_dict['month'] = date.month
            context_dict['day'] = date.day
    except (Api.DoesNotExist, Call.DoesNotExist, AttributeError):
        pass

    return render_to_response('SIL/action.html', context_dict, context)
