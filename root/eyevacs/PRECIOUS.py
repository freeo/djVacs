#good example for usage of the template object
#no template.html FILE needed!

def eye(request):
    tcontext = (request.session['django_language'], ''.join([exp.name for exp in Experiment.objects.all()]))
    tstring = Template('{% block body %}Chosen Language: {{lang}} <br>Experiments:{{exp_list}} {% endblock %}')
    cont = Contet({'lang':tcontext[0],'exp_list':tcontext[1]})
    return HttpResponse(tstring.render(cont))

#clean list comprehension for exp.names!
[exp.name for exp in Experiment.objects.all()]

#this made me lol :)
    html_temp =  '<html><body>%s</body></html>'
    mycontext = Context({'context1':'omgomgomgogm','context2':'more omgomgomgogm in context 2!!!','context3':'EVEN MORE CONTEXT!!! I CANT BELIVE IT!!!','context4':'omg. this stuff just works. friggin. unbelievable'})
    return render_to_response('eyevacs/pcpt.html', mycontext)
    #return HttpResponse( html_temp % request)
    #return render('base.html', {'body':f})
