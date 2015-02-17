from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from apis import trello
from SIL.models import User, ApiCredential, Api


def index(request):
    context = RequestContext(request)
    context_dict = {'mainmessage': "Explore Third Party APIs!"}
    return render_to_response('SIL/index.html', context_dict, context)


def api(request, api_name):
    context = RequestContext(request)

    context_dict = {'api_name': api_name}

    try:
        api = Api.objects.get(name=api_name)
        context_dict['api'] = api
        context_dict['calls'] = api.calls
    except Api.DoesNotExist:
        pass

    return render_to_response('SIL/api.html', context_dict, context)


"""def get_all_boards(request):
    context = RequestContext(request)
    context_dict = trello.
    return render_to_response('SIL/get_all_boads.html', context_dict, context)"""