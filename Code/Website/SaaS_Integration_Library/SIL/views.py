from django.http import HttpResponse

def index(request):
	return HttpResponse("SaaS Integration Libary says hello!")
