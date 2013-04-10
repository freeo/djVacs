from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
#    return render_to_response('index.html')
    # return HttpResponse('Project root index.html')
    # return HttpResponse('<a href="./eye/">Eyetracking Vacations</a>')
    return render(request, 'index.html', RequestContext(request))
