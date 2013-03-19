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
bt_label = ugettext("Continue")
validation = False
singlepagedebug = False
selectwelcome = ""

def allUrls():
    outputlist = []
    outputlist.append(reverse('eyevacs.views.welcome', args= [str(curr_exp.id)]))
    outputlist.append(reverse('eyevacs.views.rnd_max', args = [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.rnd_regret', args= [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.pl_experience', args= [str(curr_exp.id), str(pcpt.pcpt_id)]))
    outputlist.append(reverse('eyevacs.views.rnd_involvement', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_overview', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_food', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_recommend', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_distance', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_price', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_room', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_favattributes', args= [curr_exp.id, pcpt.pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_choicetasks', args= [curr_exp.id, pcpt.pcpt_id]))
    for i in range(0,len(pcpt.ctlist),1):
        outputlist.append(reverse('eyevacs.views.decisionsequence', args= [curr_exp.id, pcpt.pcpt_id, i]))
    outputlist.append(reverse('eyevacs.views.conjoint', args = [curr_exp.id, pcpt.pcpt_id, 0]))
    outputlist.append(reverse('eyevacs.views.conjoint', args = [curr_exp.id, pcpt.pcpt_id, 1]))
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
    return render(request, 'eyevacs/i18n_choose_lan.html', {'redirect_to':'./'})

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
    pcpt.initExp(exp_id)
    next_condition = pcpt.getGroup(pcpt_id)
    all_context = Context({'tasksize':tasksize,'exp_id':exp_id,'pcpt_id':pcpt_id, 'exp_name':name, 'exp':curr_exp})
    destination = reverse('eyevacs.views.preparePcpt', args= [str(curr_exp.id)])
    all_context['destination'] = destination
    all_context['next_condition'] = next_condition
    return render(request, 'eyevacs/exp.html', all_context)

def singlePageDebug(request, exp_id):
    data = {}
    data['pages'] = allUrls()
    data['lang'] = request.session['django_language']
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
    global selectwelcome
    global selectcondition
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
    if request.session.get('selectwelcome') != None:
        selectwelcome = request.session.get('selectwelcome')[0]
    if request.session.get('selectcondition') != None:
        selectcondition = request.session.get('selectcondition')[0]
    selectlanguage = request.session.get('selectlanguage')[0]
    request.session['django_language'] = selectlanguage
    ct_size = request.session['ct_size'][0]
    valid_input = request.session['input_pcptid'][0]
    pcpt.initPcpt(ct_size, valid_input, selectcondition)
    return getRedirectURL('preparePcpt')

def welcome(request, exp_id):
    if selectwelcome == "welcome_scrollable":
        destination = reverse('eyevacs.views.rnd_max', args = [str(curr_exp.id), str(pcpt.pcpt_id)])
        anydict = {'destination':destination,'bt_label':bt_label}
        # debugpostdata(anydict, 'POST:', request.POST, 'SESSION:', request.session.items())
        return render_to_response('eyevacs/1welcome_scrollable.html', RequestContext(request, anydict ))
    if selectwelcome == "welcome_paginated":
        destination = reverse('eyevacs.views.welcome_paginated', args = [curr_exp.id, 0])
        return HttpResponseRedirect(destination)

def welcome_paginated(request, exp_id, wel_page):
    pass

def rnd_max(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = {}
    ########################################################################
    # lang = request.session['django_language']
    # reqcontext['language'] = 'language: '+ lang +'\n-------------\n'
    ########################################################################
    # reqcontext = pcpt.get_scale_context('rnd_max')
    destination = reverse('eyevacs.views.rnd_regret', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['destination'] = destination
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
    reqcontext['extracaption'] = extracaption
    reqcontext['validation'] = validation
    reqcontext.update(pcpt.get_scale_context('rnd_max'))
    # debugpostdata(reqcontext, 'POST:', request.POST, 'SESSION:', request.session.items())
    return render(request, 'eyevacs/scale.html', reqcontext)

def rnd_regret(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_regret')
    destination = reverse('eyevacs.views.pl_experience', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
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
    destination = reverse('eyevacs.views.explanation_overview', args= [curr_exp.id, pcpt.pcpt_id])
    reqcontext['bt_label'] = bt_label
    reqcontext['destination'] = destination
    reqcontext['validation'] = validation
    return render(request, 'eyevacs/scale.html', reqcontext)

def explanation_overview(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_food', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation0_overview.html', reqcontext)

def explanation_food(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_recommend', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation1_food.html', reqcontext)

def explanation_recommend(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_distance', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation2_recommend.html', reqcontext)

def explanation_distance(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_seaview', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation3_distance.html', reqcontext)

def explanation_seaview(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_price', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation4_seaview.html', reqcontext)

def explanation_price(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_room', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation5_price.html', reqcontext)

def explanation_room(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_favattributes', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    reqcontext['scrollable'] = True
    return render (request, 'eyevacs/explanation6_room.html', reqcontext)

def explanation_favattributes(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.explanation_choicetasks', args= [curr_exp.id, pcpt.pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    reqcontext['validation'] = validation
    return render (request, 'eyevacs/explanation7_favattributes.html', reqcontext)

def explanation_choicetasks(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    destination = reverse('eyevacs.views.decisionsequence', args= [str(curr_exp.id), str(pcpt.pcpt_id), 0])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation8_choicetasks.html', reqcontext)

########################################################################
########################################################################
########################################################################

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
    ########################################################################
    # lang = request.session['django_language']
    # data['language'] = 'language: '+ lang +'\n-------------\n'
    ########################################################################
    # debugpostdata(data,pcpt.ctlist)
    return render(request, 'eyevacs/table.html', rq)

def conjoint(request, exp_id, pcpt_id, conjoint_id):
    request.session.update(request.POST)
    conjoint = {}
    context = {}
    if int(conjoint_id) == 0:
        for i in range(0,4,1):
            conjoint[i] = pcpt.getConjoint(i)
            destination = reverse('eyevacs.views.conjoint', args = [curr_exp.id, pcpt_id, 1])
            context['starter'] = True
    if int(conjoint_id) == 1:
        for i in range(4,8,1):
            conjoint[i-4] = pcpt.getConjoint(i)
            destination = reverse('eyevacs.views.transit', args = [exp_id, pcpt_id])
            context['starter'] = False
    context['destination'] = destination
    context['bt_label'] = bt_label
    context['conjointtasks'] = conjoint
    context['validation'] = validation
    reqcontext = RequestContext(request, context)
    return render(request, 'eyevacs/conjoint.html', reqcontext)

def transit(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    data = {}
    # data['text'] = 'transit choice, holdout task 2!'
    destination = reverse('eyevacs.views.transit_select', args = [exp_id, pcpt_id])
    # destination = reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id])
    # temp = {'destination': temp_dest}
    # data['temp'] = temp
    data['lb_button_continue'] = ugettext('Proceed to selection')
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
    dynamic['validation'] = validation
    reqcontext = RequestContext(request, dynamic)
    return render(request , 'eyevacs/transit_select.html', reqcontext)

def rnd_searchgoals(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    reqcontext = pcpt.get_scale_context('rnd_searchgoals')
    destination = reverse('eyevacs.views.pl_demographics', args= [str(curr_exp.id), str(pcpt.pcpt_id)])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
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

