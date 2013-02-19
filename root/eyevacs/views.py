from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, Template
from eyevacs.models import Experiment, Participant
from django.utils.translation import ugettext
from django.utils import translation
from django.core.urlresolvers import reverse
from eyevacs import views_pcpt as pcpt
import pdb

default_page_order = []
bt_label = "Continue"
urlsequence = [
    'welcome/',
    'rnd_max/',
    'rnd_regret/',
    #'filler/',
    'pl_experience/',
    'explanation/',
    'ct0/',
    'rnd_searchgoals/',
    'rnd_happiness/',
    'pl_demographics/',
    '../../temp/']


bla = {'intro':1,'sc_max':2,'sc_regret':3, 'filler1':4,'filler2':5,'filler3':6,'pl_purchase':7,'explanation':8,'ct':9,'hc':10,'sc_searchgoals':11,'sc_happiness':12,'demographics':13,'tourn_sel':14}

def index(request):
#    return render_to_response('index.html')
    return HttpResponse('this is the TRUE index!')

#example incoming url string:

def temp(request):
    #lang = request.session['django_language']
    # return HttpResponse('You ve reached the temporary end...')
    #return render_to_response('eyevacs/1welcome.html')
    data = {}
    data['text'] = 'You ve reached the temporary end...'
    context = Context(data)
    debugpostdata(data, request.POST)
    return render(request, 'eyevacs/0preview1650.html', context)

def paginator(origin):
    #analyze the request
    #where did i come from, where do i go?
    global urlsequence
    for i in range(0, len(urlsequence),1):
        if urlsequence[i] == origin:
            return urlsequence[i+1]
            break

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

def debugpostdata(context, *args):
    debug_string = ''
    for arg in sorted(args):
        try:
            debug_string += str(arg) + '\n'
        except:
            debug_string += '---invalid str\n'
    context['debugdata'] = debug_string

def eye(request):
    #lang = translation.check_for_language(translation.get_language())
    #lang = request.session['django_language']
    lang = translation.get_language()
    exp_list = Experiment.objects.all()
    cont = Context({'lang':lang,'exp_list':exp_list})
    return render(request, 'eyevacs/eye.html', cont)

# def catchInput(request, origin):
#     request.session



def exp(request, exp_id):
    global curr_exp
    curr_exp = Experiment.objects.get(pk=exp_id)
    name = curr_exp.name
    pk = curr_exp.pk
    # sets default task size by the order!
    tsize1 = {'label':'7 tasks','checked':'', 'value':7}
    tsize2 = {'label':'14 tasks','checked':'checked', 'value':14}
    tsize3 = {'label':'21 tasks','checked':'', 'value':21}
    tasksize =[tsize1,tsize2,tsize3]
    #pcpt_id = curr_exp.grouping.counter +1
    pcpt.initPcpt(exp_id)
    #destination = '/eye/exp'+exp_id + '/pcpt'+str(pcpt.pcpt_id)+'/welcome/'
    destination = returnExp(request)
    all_context = Context({'tasksize':tasksize,'exp_id':exp_id,'pcpt_id':pcpt.pcpt_id, 'exp_name':name, 'exp':curr_exp, 'destination':destination})

    return render(request, 'eyevacs/exp.html', all_context)
    #return init_pages(request)
    #return HttpResponse('hello eyetracker')

#def initParticipant(request, exp_id):
    #Manual PCPT doesnt do anything yet
    #pcpt_id = request.POST['input_pcptid']
    #destination = paginator('pcptinit/')
    #max_scale_context = pcpt.get_scale_context('rnd_max')
    #return HttpResponseRedirect(destination)
    #stuff = str(pcpt.initPcpt(exp_id))

    #return render_to_response('eyevacs/scale.html', max_scale_context)
    #return HttpResponse(stuff)

def returnExp(request):
    request.session['ct_size'] = request.POST
    # exp_id = curr_exp.id
    destination = '/eye/exp'+str(curr_exp.id) + '/pcpt'+str(pcpt.pcpt_id)+'/welcome/'
    #return redirect(destination)
    return HttpResponseRedirect(reverse('welcome'))

def welcome(request, exp_id, pcpt_id):
    destination = '../'+ paginator('welcome/')
    #pdb.set_trace()
    debugpostdata(scale_context, request.session)
    return render_to_response('eyevacs/1welcome.html', RequestContext(request, {'destination':destination,'bt_label':bt_label}))


def rnd_max(request, exp_id, pcpt_id):
    scale_context = pcpt.get_scale_context('rnd_max')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_max/')
    scale_context['destination'] =  destination
    debugpostdata(scale_context, request.POST)
    return render(request, 'eyevacs/scale.html', scale_context)

def rnd_regret(request, exp_id, pcpt_id):
    scale_context = pcpt.get_scale_context('rnd_regret')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_regret/')
    scale_context['destination'] =  destination
    debugpostdata(scale_context, request.POST )
    return render(request, 'eyevacs/scale.html', scale_context)

def pl_experience(request, exp_id, pcpt_id):
    destination = '../'+paginator('pl_experience/')
    #bt_label = 'Continue' #ugettext('Continue')
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/pl_experience.html', reqcontext)

def explanation(request, exp_id, pcpt_id):
    destination = '../'+paginator('explanation/')
    #bt_label = 'Continue' #ugettext('Continue')
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/explanation.html', reqcontext)

def decisionsequence(request, exp_id, pcpt_id, ct_page):
    #context['info'] = pcpt object erstellen!!! am besten ein dict...
    data = {}
    data['text'] = 'temp'
    context = Context(data)

    debugpostdata(data,pcpt.ctasklist)
    return render(request, 'eyevacs/0preview1650.html', context)



def rnd_searchgoals(request, exp_id, pcpt_id):
    scale_context = pcpt.get_scale_context('rnd_searchgoals')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_searchgoals/')
    scale_context['destination'] =  destination
    debugpostdata(scale_context, request.POST)
    return render(request, 'eyevacs/scale.html', scale_context)

def rnd_happiness(request, exp_id, pcpt_id):
    scale_context = pcpt.get_scale_context('rnd_happiness')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_happiness/')
    scale_context['destination'] =  destination
    debugpostdata(scale_context, request.POST)
    return render(request, 'eyevacs/scale.html', scale_context)

def pl_demographics(request, exp_id, pcpt_id):
    destination = '../'+paginator('pl_demographics/')
    #bt_label = 'Continue' #ugettext('Continue')
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/pl_demographics.html', reqcontext)

def pcptInfo(request, exp_id, pcpt_id):
    return HttpRespones(Participant.objects.get(pk = pcpt_id))
    #return render_to_response('eyevacs/scale.html')

