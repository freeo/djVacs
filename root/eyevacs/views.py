from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, Template
from eyevacs.models import Experiment, Participant
from django.utils.translation import ugettext
from django.utils import translation
from django.core.urlresolvers import reverse
from eyevacs import views_pcpt as pcpt
from django.contrib.sessions.models import Session
import pdb

curr_exp = None
default_page_order = []
bt_label = "Continue"
urlsequence = [
    'eyevacs.views.welcome',
    'eyevacs.views.rnd_regret',
    'eyevacs.views.rnd_regret',
    #'filler/',
    'eyevacs.views.pl_experience',
    'eyevacs.views.explanation',
    #ct system, not yet designed
    'eyevacs.views.ct0',
    'eyevacs.views.rnd_searchgoals',
    'eyevacs.views.rnd_happiness',
    'eyevacs.views.pl_demographics',
    'eyevacs.views.temp']

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

# def errorTemp(request):

def paginator(origin):
    #analyze the request
    #where did i come from, where do i go?
    global urlsequence
    for i in range(0, len(urlsequence),1):
        if urlsequence[i] == origin:
            return urlsequence[i+1]
            break

def arginator(Page):
    nextPageArgs
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
    for arg in args:
        try:
            debug_string += str(arg) + '\n'
        except:
            debug_string += '---invalid str\n'
    context['debugdata'] = debug_string

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
    return errors

def eye(request):
    #lang = translation.check_for_language(translation.get_language())
    #lang = request.session['django_language']
    lang = translation.get_language()
    exp_list = Experiment.objects.all()
    cont = Context({'lang':lang,'exp_list':exp_list})
    return render(request, 'eyevacs/eye.html', cont)

def exp(request, exp_id):
    validlist = ['ct_size','input_pcptid']
    missingPostData = validate(request.POST, validlist)
    if len(validlist) == len(missingPostData):
        newPage = True
    else:
        newPage = False
    if missingPostData:
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
        all_context = Context({'tasksize':tasksize,'exp_id':exp_id,'pcpt_id':pcpt.pcpt_id, 'exp_name':name, 'exp':curr_exp})
        if not newPage:
            all_context['error'] = missingPostData
        return render(request, 'eyevacs/exp.html', all_context)
    else:
        request.session.update(request.POST)
        destination = reverse('eyevacs.views.welcome', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
        return HttpResponseRedirect(destination)

'''
def returnExp(request, exp_id):
    request.session['exp'] = request.POST
    # exp_id = curr_exp.id
    # destination = '/eye/exp'+str(curr_exp.id) + '/pcpt'+str(pcpt.pcpt_id)+'/welcome/'
    destination = reverse(welcome, args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    # simple = reverse(temp)
    # return HttpResponse('Selected ct_size: %s' % request)
    return HttpResponseRedirect(destination)
    #return HttpResponseRedirect(reverse('welcome', kwargs= {'exp_id':str(curr_exp.id), 'pcpt_id':str(pcpt.pcpt_id)}))
'''

def welcome(request, exp_id, pcpt_id):
    #clear the cookie here for contingency and so exp can be revisited back and forth
    # request.session.clear()
    destination = reverse('eyevacs.views.rnd_max', args = [str(curr_exp.id), str(pcpt.pcpt_id)])
    anydict = {'destination':destination,'bt_label':bt_label}
    debugpostdata(anydict, 'POST:', request.POST, 'SESSION:', request.session.items())
    return render_to_response('eyevacs/1welcome.html', RequestContext(request, anydict ))

def restoreExistingData(reqcontext, validlist, missingPostData, cookie):
    restorable = []
    for item in validlist:
        if item not in missingPostData:
            restorable.append(item)
    for r in restorable:
        print cookie[r]

def rnd_max(request, exp_id, pcpt_id):
    validlist = ['rnd_maxQ1','rnd_maxQ2','rnd_maxQ3','rnd_maxQ4','rnd_maxQ5','rnd_maxQ6']
    missingPostData = validate(request.POST, validlist)
    if len(validlist) == len(missingPostData):
        newPage = True
    else:
        newPage = False
    if missingPostData:
        reqcontext = pcpt.get_scale_context('rnd_max')
        # restoreExistingData(reqcontext, validlist, missingPostData, request.session)
        debugpostdata(reqcontext, 'POST:', request.POST, 'SESSION:', request.session.items())
        if not newPage:
            reqcontext['error'] = missingPostData
        return render(request, 'eyevacs/scale.html', reqcontext)
    else:
        request.session.update(request.POST)
        destination = reverse('eyevacs.views.rnd_regret', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
        return HttpResponseRedirect(destination)

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


def pl_experience(request, exp_id, pcpt_id):
    validlist = ['rnd_regretQ1','rnd_regretQ2','rnd_regretQ3','rnd_regretQ4','rnd_regretQ5']
    missingPostData = validate(request.POST, validlist)
    if len(validlist) == len(missingPostData):
        newPage = True
    else:
        newPage = False
    if missingPostData:
        #bt_label = 'Continue' #ugettext('Continue')
        site_vars = {'bt_label':bt_label}
        reqcontext = RequestContext(request, site_vars)
        debugpostdata(reqcontext, 'POST:', request.POST, 'SESSION:', request.session.items())
        if not newPage:
            reqcontext['error'] = missingPostData
        return render (request, 'eyevacs/pl_experience.html', reqcontext)
    else:
        request.session.update(request.POST)
        destination = reverse('eyevacs.views.explanation', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
        return HttpResponseRedirect(destination)



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
    reqcontext = pcpt.get_scale_context('rnd_searchgoals')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_searchgoals/')
    reqcontext['destination'] =  destination
    debugpostdata(reqcontext, request.POST)
    return render(request, 'eyevacs/scale.html', reqcontext)

def rnd_happiness(request, exp_id, pcpt_id):
    reqcontext = pcpt.get_scale_context('rnd_happiness')
    #stuff = str(pcpt.initPcpt(exp_id))
    destination = '../'+paginator('rnd_happiness/')
    reqcontext['destination'] =  destination
    debugpostdata(reqcontext, request.POST)
    return render(request, 'eyevacs/scale.html', reqcontext)

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

