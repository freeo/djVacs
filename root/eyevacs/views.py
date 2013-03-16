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
validation = False
singlepagedebug = False

def allUrls():
    outputlist = []
    outputlist.append(reverse('eyevacs.views.welcome', args= [str(curr_exp.id)]))
    outputlist.append(reverse('eyevacs.views.rnd_max', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.rnd_regret', args= [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.pl_experience', args= [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.rnd_involvement', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation', args= [str(curr_exp.id), str(pcpt.pcpt_id)]))
    for i in range(0,len(pcpt.ctlist),1):
        outputlist.append(reverse('eyevacs.views.decisionsequence', args= [curr_exp.id, pcpt.pcpt_id, i]))
    for j in range(0,len(pcpt.conjoint),1):
        outputlist.append(reverse('eyevacs.views.conjoint', args = [curr_exp.id, pcpt.pcpt_id, j]))
    outputlist.append(reverse('eyevacs.views.transit', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.transit_select', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.rnd_searchgoals', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    # outputlist.append(reverse('eyevacs.views.rnd_happiness', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.pl_demographics', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.finalPage', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    return outputlist

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
    # if request.POST == {}:
    global curr_exp
    curr_exp = Experiment.objects.get(pk=exp_id)
    name = curr_exp.name
    pk = curr_exp.pk
    # sets default task size by the order!
    tasksize =[]
    tsize1 = {'label':'7 tasks','checked':'checked', 'value':7}
    tasksize.append(tsize1)
    tsize2 = {'label':'14 tasks','checked':'', 'value':14}
    tasksize.append(tsize2)
    # tsize3 = {'label':'21 tasks','checked':'', 'value':21}
    # tasksize.append(tsize3)
    # pcpt.pcpt_id
    #usual order id:
    pcpt_id = curr_exp.grouping.counter
    all_context = Context({'tasksize':tasksize,'exp_id':exp_id,'pcpt_id':pcpt_id, 'exp_name':name, 'exp':curr_exp})
    destination = reverse('eyevacs.views.preparePcpt', args= [str(curr_exp.id)])
    all_context['destination'] = destination
    return render(request, 'eyevacs/exp.html', all_context)

def singlePageDebug(request, exp_id):
    data = {}
    data['pages'] = allUrls()
    context = RequestContext(request, data)
    return render(request, 'eyevacs/debug.html', context)


def getRedirectURL(source):
    if source == 'preparePcpt':
        if singlepagedebug:
            destination = reverse('eyevacs.views.singlePageDebug', args= [str(curr_exp.id)])
        else:
            destination = reverse('eyevacs.views.welcome', args= [str(curr_exp.id)])
        return HttpResponseRedirect(destination)

def preparePcpt(request, exp_id):
    #expects POST data
    #gets stored as list! need [0]
    global validation
    global singlepagedebug
    request.session.clear()
    request.session.update(request.POST)
    if request.session.get('cbox_validation') != None:
        #cbox value is redundant!!! May be anything.
        validation = True
    else:
        validation = False
    if request.session.get('cbox_singlepagedebug') != None:
        singlepagedebug = True
    else:
        singlepagedebug = False
    ct_size = request.session['ct_size'][0]
    valid_input = request.session['input_pcptid'][0]
    pcpt.initPcpt(exp_id, ct_size, valid_input)
    return getRedirectURL('preparePcpt')
    data = {}
    data['text'] = str(request.session.items())
    # temp_dest = reverse('eyevacs.views.transit', args = [exp_id, pcpt_id])
    # temp = {'destination': temp_dest}
    # data['temp'] = temp
    context = Context(data)
    # return render(request, 'eyevacs/0preview1650.html', context)

def welcome(request, exp_id):
    destination = reverse('eyevacs.views.rnd_max', args = [str(curr_exp.id), str(pcpt.pcpt_id)])
    anydict = {'destination':destination,'bt_label':bt_label}
    debugpostdata(anydict, 'POST:', request.POST, 'SESSION:', request.session.items())
    return render_to_response('eyevacs/1welcome.html', RequestContext(request, anydict ))

def rnd_max(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_max')
    destination = reverse('eyevacs.views.rnd_regret', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['destination'] = destination
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':'I do not agree at all', 'right':'I agree very much'}
    reqcontext['extracaption'] = extracaption
    # reqcontext['caption1_right'] = 'I agree very much'
    reqcontext['validation'] = validation
    # debugpostdata(reqcontext, 'POST:', request.POST, 'SESSION:', request.session.items())
    return render(request, 'eyevacs/scale.html', reqcontext)

def rnd_regret(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_regret')
    destination = reverse('eyevacs.views.pl_experience', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':'I do not agree at all', 'right':'I agree very much'}
    reqcontext['extracaption'] = extracaption
    reqcontext['destination'] = destination
    reqcontext['validation'] = validation
    return render(request, 'eyevacs/scale.html', reqcontext)

def pl_experience(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    site_vars = {'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    destination = reverse('eyevacs.views.rnd_involvement', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['destination'] = destination
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/pl_experience.html', reqcontext)

def rnd_involvement(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_involvement')
    destination = reverse('eyevacs.views.explanation', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['bt_label'] = bt_label
    reqcontext['destination'] = destination
    reqcontext['validation'] = validation
    return render(request, 'eyevacs/scale.html', reqcontext)

def explanation(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.decisionsequence', args= [str(curr_exp.id), str(pcpt.pcpt_id), 0])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/explanation.html', reqcontext)

# def initsequence(request, exp_id, pcpt_id):
#     request.session['taskcounter'] = 0
#     taskcounter = request.session['taskcounter']
#     destination = reverse('eyevacs.views.decisionsequence', args = [curr_exp.id, pcpt_id, taskcounter])
#     return HttpResponseRedirect(destination)

def decisionsequence(request, exp_id, pcpt_id, ct_page):
    request.session.update(request.POST)
    #context['info'] = pcpt object erstellen!!! am besten ein dict...
    data = {}
    #just a debug variable for special purposes
    data['text'] = ''
    data['taskcounter'] = pcpt.taskcounter
    ctdict = pcpt.getTask(int(ct_page))
    data.update(ctdict)
    rq = RequestContext(request, data)
    if pcpt.checkNextTask(int(ct_page)):
        next_page = int(ct_page) + 1
        destination = reverse('eyevacs.views.decisionsequence', args = [curr_exp.id, pcpt_id, next_page])
    else:
        destination = reverse('eyevacs.views.conjoint', args = [exp_id, pcpt_id, 0])
    data['destination'] = destination
    debugpostdata(data,pcpt.ctlist)
    return render(request, 'eyevacs/table.html', rq)

# def validateTask(request, exp_id, pcpt_id, ct_page):
#     #post contains hidden:
#     ct_id = request.POST.get('ct_id')
#     request.session.update(request.POST)
#logic: which aX was selected? its ID?
#dict request.session['choices'].push( id:aX )

def conjoint(request, exp_id, pcpt_id, conjoint_id):
    request.session.update(request.POST)
    context = {}
    context['conjoint'] = pcpt.getConjoint(int(conjoint_id))
    context['conjoint']['id'] = conjoint_id
    if pcpt.checkNextConjoint(int(conjoint_id)):
        next_conjoint = int(conjoint_id) + 1
        destination = reverse('eyevacs.views.conjoint', args = [curr_exp.id, pcpt_id, next_conjoint])
    else:
        destination = reverse('eyevacs.views.transit', args = [exp_id, pcpt_id])
    if int(conjoint_id) == 0:
        context['starter'] = True
    context['destination'] = destination
    context['bt_label'] = bt_label
    context['extracaption'] = {'left':'0: definitely reject','right':'10: definitely accept'}
    context['validation'] = validation
    reqcontext = RequestContext(request, context)
    return render(request, 'eyevacs/conjoint.html', reqcontext)

    data = {}
    data['text'] = 'holdout task 1 pages'
    temp_dest = reverse('eyevacs.views.transit', args = [exp_id, pcpt_id])
    temp = {'destination': temp_dest}
    data['temp'] = temp
    context = Context(data)
    return render(request, 'eyevacs/0preview1650.html', context)

def transit(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    data = {}
    # data['text'] = 'transit choice, holdout task 2!'
    destination = reverse('eyevacs.views.transit_select', args = [exp_id, pcpt_id])
    # destination = reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id])
    # temp = {'destination': temp_dest}
    # data['temp'] = temp
    data['lb_button_continue'] = 'Proceed to selection'
    data['destination'] = destination
    context = Context(data)
    return render(request, 'eyevacs/transitOverview.html', context)

def hotel1(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel1.html', Context())
def hotel2(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel2.html', Context())
def hotel3(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel3.html', Context())
def hotel4(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel4.html', Context())
def hotel5(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel5.html', Context())
def hotel6(request, exp_id, pcpt_id):
    return render_to_response('eyevacs/hotel6.html', Context())

def transit_select(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    dynamic = {}
    destination = reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id])
    dynamic['destination'] = destination
    dynamic['bt_label'] = bt_label
    reqcontext = RequestContext(request, dynamic)
    return render(request , 'eyevacs/transit_select.html', reqcontext)

def rnd_searchgoals(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_searchgoals')
    destination = reverse('eyevacs.views.pl_demographics', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':'I do not agree at all', 'right':'I agree very much'}
    reqcontext['extracaption'] = extracaption
    reqcontext['destination'] = destination
    reqcontext['validation'] = validation
    return render(request, 'eyevacs/scale.html', reqcontext)

def rnd_happiness(request, exp_id, pcpt_id):
    pass
    # sorry happiness scale... you're out.
    # request.session.update(request.POST)
    # reqcontext = pcpt.get_scale_context('rnd_happiness')
    # destination = reverse('eyevacs.views.pl_demographics', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    # reqcontext['bt_label'] = bt_label
    # reqcontext['destination'] = destination
    # reqcontext['validation'] = validation
    # return render(request, 'eyevacs/scale.html', reqcontext)

def pl_demographics(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.finalPage', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    # debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/pl_demographics.html', reqcontext)

def finalPage(request, exp_id, pcpt_id):
    request.session.update(request.POST)

    return render (request, 'eyevacs/thankyou.html')

    # data = {}
    # data['text'] = 'Thank You for your participation!'
    # temp_dest = reverse('eyevacs.views.', args = [exp_id, pcpt_id])
    # temp = {'destination': temp_dest}
    # temp = {'somekey': 'sometext'}
    # data['temp'] = temp
    # context = Context(data)
    # return render(request, 'eyevacs/0preview1650.html', context)

def pcptInfo(request, exp_id, pcpt_id):
    return HttpRespones(Participant.objects.get(pk = pcpt_id))
    #return render_to_response('eyevacs/scale.html')

