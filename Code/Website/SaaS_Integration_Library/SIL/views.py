from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from apis import trello
from SIL.models import ApiCredential

def index(request):
	context = RequestContext(request)
	context_dict = {'mainmessage': "Explore Third Party APIs!"}
	return render_to_response('SIL/index.html', context_dict, context)



"""def get_all_boards(request):
    context = RequestContext(request)
    context_dict = trello.
    return render_to_response('SIL/get_all_boads.html', context_dict, context)"""