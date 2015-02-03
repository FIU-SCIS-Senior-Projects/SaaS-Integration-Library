from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	
	context_dict = {'mainmessage': "Explore Third Party APIs!"}
	return render_to_response('SIL/index.html', context_dict, context)
