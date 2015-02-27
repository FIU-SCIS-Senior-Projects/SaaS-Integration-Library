from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

import simplejson

from apis import trello
from SIL.models import ApiCredential, Api, Call


def index(request):
    context = RequestContext(request)
    context_dict = {'mainmessage': "Explore Third Party APIs!"}
    return render_to_response('SIL/index.html', context_dict, context)

def datasets(request):
    context = RequestContext(request)

    context_dict = {}
    # try:
    #
    # except AttributeError:
    #     pass

    return render_to_response('SIL/datasets.html', context_dict, context)

def api(request, api_name):
    context = RequestContext(request)

    context_dict = {'api_name': api_name}

    try:
        api = Api.objects.get(name=api_name.lower())
        cred = api.credentials
        context_dict['api'] = api

        #loop through calls to clear out '_'s between names
        context_dict['calls'] = {}
        for call in api.calls:
            context_dict['calls'][call] = call.replace('_', ' ')
        context_dict['credentials'] = cred.settings['token']
    except Api.DoesNotExist:
        pass

    return render_to_response('SIL/api.html', context_dict, context)


def apicall(request, api_name, action_name):
    context = RequestContext(request)

    action = action_name.replace('_', ' ')          #name to display

    context_dict = {'action_name': action_name}

    try:
        #need if to check whether api credentials exist already?
        #Get the Api object, then obtain the credentials from the given Api and create object to make calls
        api = Api.objects.get(name=api_name.lower())
        api_tok = api.credentials.settings['token']
        api_obj = trello.Trello(api_tok)

        #if the call exists already, delete it to make more recent call
        if Call.objects.filter(name=action_name) is not None:
            Call.objects.filter(name=action_name).delete()

        #what about if call requires argument?
        #create call object to as to return
        call = Call.objects.create(api=api,name=action_name, response=getattr(api_obj, action_name)())
        context_dict['call'] = call
        #TODO make json dump pretty
        context_dict['response'] = simplejson.dumps(call.response)#HttpResponse(simplejson.dumps(call.response),content_type="application/json")
        context_dict['action'] = action.upper()

    except (Api.DoesNotExist, Call.DoesNotExist, AttributeError):
        pass

    return render_to_response('SIL/action.html', context_dict, context)
