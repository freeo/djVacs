from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import Context, Template
from eyevacs.models import Experiment, Participant
from django.utils.translation import ugettext
from django.utils import translation
from eyevacs import views_pcpt as pcpt

default_page_order = []
page_sequence = {'intro':1,'sc_max':2,'sc_regret':3, 'filler1':4,'filler2':5,'filler3':6,'pl_purchase':7,'explanation':8,'ct':9,'hc':10,'sc_searchgoals':11,'sc_happiness':12,'demographics':13,'tourn_sel':14}

def index(request):
#    return render_to_response('index.html')
    return HttpResponse('this is the TRUE index!')

#example incoming url string:
#/exp1/pcpt1/pg1/

def eye(request):
    #if request.LANGUAGE
    #translation.activate('de')
    lang = translation.check_for_language(translation.get_language())
    #lang = request.session['django_language']
    #lang = translation.get_language()
    exp_list = Experiment.objects.all()
    cont = Context({'lang':lang,'exp_list':exp_list})
    return render(request, 'eyevacs/eye.html', cont)

#set language and create participant, show experiment info!
#Idee: /x/lang/ fuer jedes x! redirect_to = x also zurueck /x/
def set_language(request):
    #inits language
    #request.session['django_language']
    translate_example = ugettext('This string has to be translated. It was marked with ugettext().')
    postnext = {'next':'www.google.de'}
    mycopy = request.POST.copy()
    mycopy.update(postnext)
    return render(request, 'eyevacs/i18n_choose_lan.html', {'redirect_to':'/eye/'})

def temp(request):
    lang = request.session['django_language']
    return HttpResponse('language selected: %s' % lang )

def experiment_id(request, exp_id):
    curr_exp = Experiment.objects.get(pk=exp_id)
    name = curr_exp.name
    pk = curr_exp.pk
    info_list = ['vorname','name','alter']
    pcpt_id = 1
    all_context = Context({'info_list':info_list,'exp_id':exp_id,'pcpt_id':pcpt_id, 'exp_name':name, 'exp':curr_exp})
    return render(request, 'eyevacs/initpcpt.html', all_context)
    #return init_pages(request)
    #return HttpResponse('hello eyetracker')

def initParticipant(request, exp_id ):
    pcpt_id = request.POST['input_pcptid']
    pcpt.initPcpt(exp_id)
    max_scale_context = pcpt.get_scale_context('rnd_regret')
    #stuff = str(pcpt.initPcpt(exp_id))

    return render_to_response('eyevacs/scale.html', max_scale_context)
    #return HttpResponse(stuff)

def participant(request, exp_id, pcpt):
    return render_to_response('eyevacs/scale.html')

def page(request, exp_id, pcpt, page):
    getPage(p)
