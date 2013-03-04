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


'''Meine Eigene Version von Form Validierung! Eigentlich recht elegant. Es wird leider dem Anspruch nicht gerecht, dass ich eine grosse HTML Matrix praezise ansteuern muss... Loesung: Javascript bzw. jQuery mit dem Plugin "Validation". Aus historischem Grund hier meine Version und natuerlich auch, weil es mich Arschviel Zeit gekostet hat und ich es deshalb nicht verloren gehen lassen darf...:'''

def validate(post, validlist):
    #post: gegebene daten key,value
    #validlist: needed data key only
    errors = []
    for validitem in validlist:
        if not validitem in post:
            errors.append(validitem)
        else:
            if post[validitem] == '':
                errors.append(validitem)
    return error

def rnd_regret(request, exp_id, pcpt_id):
    validlist = ['rnd_regretQ1','rnd_regretQ2','rnd_regretQ3','rnd_regretQ4','rnd_regretQ5']
    missingPostData = validate(request.POST, validlist)
    if len(validlist) == len(missingPostData):
        newPage = True
    else:
        newPage = False
    if missingPostData:
        reqcontext = pcpt.get_scale_context('rnd_regret')
        debugpostdata(reqcontext, 'POST:', request.POST, 'SESSION:', request.session.items())
        if not newPage:
            reqcontext['error'] = missingPostData
        return render(request, 'eyevacs/scale.html', reqcontext)
    else:
        request.session.update(request.POST)
        destination = reverse('eyevacs.views.pl_experience', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
        return HttpResponseRedirect(destination)

[...]
<form action="" method="post" name="{{scale_name}}" id="{{scale_id}}">{% csrf_token %}
[...]
