from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, Template
from eyevacs.models import Experiment, Participant, Pub
from django.utils.translation import ugettext, ugettext_lazy
from django.utils import translation
from django.core.urlresolvers import reverse
from eyevacs import views_pcpt as pcpt
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
from django.forms.models import model_to_dict
from django.db import transaction
from threading import Thread
import subprocess
import operator
import pdb

default_page_order = []
bt_label = ugettext_lazy("Continue")
# validation = False
# singlepagedebug = False
selectwelcome = ""

def allUrls(pcpt_id, exp_id, ctlist):
    outputlist = []
    outputlist.append(reverse('eyevacs.views.welcome', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.rnd_max', args = [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.rnd_regret', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.pl_experience', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.rnd_involvement', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_overview', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_food', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_recommend', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_distance', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_price', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_room', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_favattributes', args= [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.explanation_ctseqintro', args= [exp_id, pcpt_id]))
    for i in range(0,len(ctlist),1):
    # for i in range(0,len(pcpt.ctlist),1):
        outputlist.append(reverse('eyevacs.views.decisionsequence', args= [exp_id, pcpt_id, i]))
    outputlist.append(reverse('eyevacs.views.conjoint', args = [exp_id, pcpt_id, 0]))
    outputlist.append(reverse('eyevacs.views.conjoint', args = [exp_id, pcpt_id, 1]))
    # outputlist.append(reverse('eyevacs.views.transit', args = [exp_id, pcpt_id]))
    # outputlist.append(reverse('eyevacs.views.transit_select', args = [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id]))
    # outputlist.append(reverse('eyevacs.views.rnd_happiness', args = [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.pl_demographics', args = [exp_id, pcpt_id]))
    outputlist.append(reverse('eyevacs.views.finalPage', args = [exp_id, pcpt_id]))
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
    request.session.update(request.POST)
    try:
        if request.session['selectresolution'] != None:
            request.session['resolution'] = str(request.session['selectresolution'][0])
            request.session.modified = True
    except:
            request.session['resolution'] = "1280x1024"
            request.session.modified = True
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
    curr_exp = Experiment.objects.get(pk=exp_id)
    name = curr_exp.name
    pk = curr_exp.pk
    if curr_exp.grouping.id_holes == None:
        curr_exp.grouping.id_holes = '[]'
        curr_exp.grouping.save()
    # sets default task size by the order!
    tasksize =[]
    tsize1 = {'label':'8 tasks','checked':'checked', 'value':8, 'enabled':''}
    tasksize.append(tsize1)
    tsize2 = {'label':'16 tasks','checked':'', 'value':16, 'enabled':'disabled'}
    tasksize.append(tsize2)
    # tsize3 = {'label':'21 tasks','checked':'', 'value':21}
    # tasksize.append(tsize3)
    #usual order id:
    pcpt_id = curr_exp.grouping.counter
    # pcpt.initExp(exp_id)
    next_condition = pcpt.getGroup(exp_id, pcpt_id)
    all_context = Context({'tasksize':tasksize,'exp_id':exp_id,'pcpt_id':pcpt_id, 'exp_name':name, 'exp':curr_exp})
    destination = reverse('eyevacs.views.preparePcpt', args= [curr_exp.id])
    all_context['destination'] = destination
    all_context['next_condition'] = next_condition
    all_context['project_language'] = curr_exp.language
    all_context['exp'] = curr_exp
    all_context['used'] = pcpt.countUsedObjects(curr_exp.id)
    all_context['unused'] = pcpt.countUnusedObjects(curr_exp.id)

    #Give ALL the pubs to exp!
    pubs = curr_exp.pub_set.all()#order_by timestamp
    pubsList = []
    pub_time_list = []
    for pub in pubs:
        new_item = model_to_dict(pub)
        now = datetime.utcnow()
        # t_delta = now - new_item['create_time'].today()
        t_delta = now - new_item['create_time'].replace(tzinfo=None)
        # t_delta.resolution = timedelta(seconds=1)
        new_item['time_string'] = str(t_delta.seconds / 60) + 'mins ago'
        pubsList.append(new_item)
    all_context['pubs'] = sorted(pubsList)
    all_context['remove_pubs_url'] = reverse('eyevacs.views.removepubs', args=[curr_exp.id])
    all_context['id_holes'] = curr_exp.grouping.id_holes #textfield!
    all_context['url_reset_id_holes'] = reverse('eyevacs.views.resetIDholes', args=[curr_exp.id])
    all_context['next_id_hole'] = pcpt.get_next_id_hole(curr_exp.id)
    all_context['next_id_hole_group'] = pcpt.getGroup(curr_exp.id, pcpt.get_next_id_hole(curr_exp.id))
    all_context['id_hole_groups'] = str(pcpt.get_id_hole_groups(curr_exp.id))
    all_context['grouping'] = curr_exp.grouping.group_nr[1:50]
    request.session.create()
    request.session['debug_pubs'] = pubsList
    return render(request, 'eyevacs/exp.html', all_context)

def removepubs(request, exp_id):
    '''removes all links and pubs from POST given IDs to delete. Redirects, after deletion.'''
    pubs_to_delete_string = request.POST.getlist('pubs_to_delete')
    #list comprehension
    pubs_to_delete_id = [int(x) for x in pubs_to_delete_string]
    pubs_objects = []
    for delete_this_pub_id in pubs_to_delete_id:
        pubs_objects.append(Pub.objects.get(pk=delete_this_pub_id))
    with transaction.commit_on_success():
        for pub in pubs_objects:
            pub_cts = pub.Choice_TasksAsPub.all() #all makes a queryset from the related manager. needed because the latter isn't iterable.
            pub_scales = pub.external_order_scale_set.all()
            try:
                pub_bsl_id_hard = pub.Baseline_Choice_TasksAsPub.all()[0].id_hard
                pub_bsl_source_file = pub.Baseline_Choice_TasksAsPub.all()[0].ext_src_data
                pub_bsls = pub_bsl_source_file.external_baseline_choice_task_set.filter(id_hard = pub_bsl_id_hard).order_by('pk')
            except:
                pub_bsls = []
            objects = [pub_cts, pub_scales, pub_bsls]
            for o in objects: #each objects
                for e in o: #each linked item of each object
                    e.linked_pub = None
                    e.used = False
                    e.save()
            #add deleted hard_id's to grouping.id_holes
            pcpt.add_id_hole(exp_id, pub.hard_id)
            #AFTER unlinking, otherwise the linked models get lost!
            pub.delete()

    destination = reverse('eyevacs.views.exp',args= [exp_id])
    return HttpResponseRedirect(destination)

    #debug
    # pubs_after_deletion = Pub.objects.count()
    # somedice = {'text':pubs_after_deletion}
    # somedice = {'text':pubs_to_delete}
    # reqcontext = RequestContext(request,somedice)
    # tempdestination = reverse('eyevacs.views.exp',args= [curr_exp.id])
    # temp = {'destination': tempdestination}
    # reqcontext['temp'] = temp
    # return render(request, 'eyevacs/0preview1650.html', reqcontext)

def resetIDholes(request, exp_id):
    pcpt.reset_id_holes(exp_id)

    destination = reverse('eyevacs.views.exp',args= [exp_id])
    return HttpResponseRedirect(destination)



def singlePageDebug(request, exp_id, pcpt_id):
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True
    data = {}
    pub = Pub.objects.get(experiment=exp_id,hard_id=pcpt_id)
    ctlist = request.session['pub_ctlist']
    data['pub'] = pub
    data['pages'] = allUrls(pcpt_id, exp_id, ctlist)
    data['lang'] = request.session['django_language']
    context = RequestContext(request, data)
    return render(request, 'eyevacs/debug.html', context)

def getRedirectURL(request, source, exp_id, pcpt_id):
    '''
    Set benchmarkSQL for extra page before welcome, to enter debug toolbar for
    SQL performance.
    '''
    benchmarkSQL = 0
    if source == 'preparePcpt':
        if request.session['singlepagedebug']:
            destination = reverse('eyevacs.views.singlePageDebug', args= [exp_id, pcpt_id])
        else:
            destination = reverse('eyevacs.views.welcome', args= [exp_id, pcpt_id])
        #SQL Benchmarking:
        if benchmarkSQL:
            data = {}
            data['text'] = 'Participant created. Go to next page:'
            temp = {'destination': destination}
            data['temp'] = temp
            reqcontext = RequestContext(request,data)
            return render(request, 'eyevacs/0preview1650.html', reqcontext)
            # text = '<a href="'+destination+'">Continue</a>'
            # return HttpResponse(text)
        # Normally:
        else:
            return HttpResponseRedirect(destination)

def preparePcpt(request, exp_id):
    #expects POST data
    #gets stored as list! need [0]
    # global singlepagedebug
    # global selectwelcome
    # global selectcondition
    # request.session.clear()
    # request.session.flush()
    request.session.create()
    request.session.update(request.POST)
    request.session['timestamps'] = {request.path:datetime.utcnow()}
    # request.session['timestamps'] = {createUniqueKey(request):datetime.utcnow()}
    # grabs from POST, not session. only explanation, not verified
    if request.session.get('cbox_validation') != None:
        request.session['validation'] = True
    else:
        request.session['validation'] = False
    try:
        del request.session['cbox_validation']
    except:
        pass

    if request.session.get('cbox_singlepagedebug') != None:
        request.session['singlepagedebug'] = True
    else:
        request.session['singlepagedebug'] = False
    try:
        del request.session['cbox_singlepagedebug']
    except:
        pass

    # if request.session.get('selectwelcome') != None:
    #     selectwelcome = request.session.get('selectwelcome')[0]
    if request.session.get('selectcondition') != None:
        selectcondition = request.session.get('selectcondition')[0]
    try:
        del request.session['selectcondition']
    except:
        pass

    if request.session.get('cbox_valid_pcpt') != None:
        request.session['valid_pcpt'] = True
        del request.session['cbox_valid_pcpt']
    else:
        request.session['valid_pcpt'] = False

    if request.session.get('cbox_testpcpt') != None:
        request.session['testpcpt'] = True
        del request.session['cbox_testpcpt']
    else:
        request.session['testpcpt'] = False

    if request.session.get('cbox_debugsaving') != None:
        debugsaving_activated = True
    else:
        debugsaving_activated = False

    # request.session['resolution'] = str(request.session.get('selectresolution')[0])
    request.session['resolution'] = str(request.session['selectresolution'][0])


    selectlanguage = request.session.get('selectlanguage')[0]
    request.session['django_language'] = selectlanguage

    # HTML stringifies all chars. Cant obtain integers from session.
    ct_size = int(request.session['ct_size'][0])

    # might be used to overwrite a corrupt pcpt (not valid one).
    # is 'future', better not use it.
    # stick to manual garbage collection of pubs
    # valid_input = request.session['input_pcptid'][0]
    # pcpt_id = pcpt.initPcpt(ct_size, request.COOKIES['sessionid'], request.COOKIES['csrftoken'], selectcondition)
    (pcpt_id, ctlist, pub, scale_sequences) = pcpt.initPcpt(exp_id, ct_size, request.session.session_key, request.COOKIES['csrftoken'], selectcondition)
    request.session['pub_pcpt_id'] = pcpt_id
    request.session['pub_ctlist'] = ctlist
    request.session['pub'] = model_to_dict(pub)
    request.session['pub_scale_sequences'] = scale_sequences
    request.session['pub_condition'] = pub.def_group
    request.session['pub_condition_override'] = pub.override_group
    request.session['pub_ctlist_IDs'] = [ct.pk for ct in ctlist]
    request.session['pub_scale_sequences_IDs'] = [rnd.pk for key, rnd in scale_sequences.iteritems()]



    #DEBUG
    #first pcpt_id entry
    # request.session['all_rnd_orderings'] = pcpt.scale_order_ids
    # request.session['all_choice_tasks'] = pcpt.ctlistIDs

    if debugsaving_activated:
        # pcpt.debugMakePCPT('increasing', pub, ctlist, scale_sequences)
        # pcpt.debugMakePCPT('baselinelow', pub, ctlist, scale_sequences)
        pcpt.debugMakePCPT('baselinehigh', pub, ctlist, scale_sequences)
        return render(request, 'eyevacs/thankyou.html')

    #DEBUG Pubs
    # lastPubID = curr_exp.pub_set.count()
    # lastPub = curr_exp.pub_set.all()[lastPubID-1]
    # request.session['pub'] = model_to_dict(lastPub)
    # cts_string = ''
    # cts = lastPub.Choice_TasksAsPub.all()
    # for ct in cts:
    #     cts_string += str(ct.pk) + ', '
    # request.session['pub_cts'] = cts_string
    # rnds = lastPub.external_order_scale_set.all()
    # rnds_count = lastPub.external_order_scale_set.count()
    # rnds_string = ''
    # for rnd in rnds:
    #     rnds_string += str(rnd.pk) + ', '
    # request.session['pub_scales'] = rnds_string

    return getRedirectURL(request, 'preparePcpt',exp_id, pcpt_id)

def welcome(request, exp_id, pcpt_id):
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True
    destination = reverse('eyevacs.views.rnd_max', args = [exp_id, pcpt_id])
    anydict = {'destination':destination,'bt_label':bt_label}
    reqcontext = RequestContext(request, anydict )
    if request.session.get('selectwelcome') != None:
        selectwelcome = request.session.get('selectwelcome')[0]
    if selectwelcome == "welcome_en":
        return render_to_response('eyevacs/1welcome_en.html', reqcontext)
    if selectwelcome == "welcome_ger":
        return render_to_response('eyevacs/1welcome_ger.html', reqcontext)

def rnd_max(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    reqcontext = {}
    ########################################################################
    # lang = request.session['django_language']
    # reqcontext['language'] = 'language: '+ lang +'\n-------------\n'
    ########################################################################
    # reqcontext = pcpt.get_scale_context('rnd_max')
    destination = reverse('eyevacs.views.rnd_regret', args= [exp_id, pcpt_id])
    reqcontext['destination'] = destination
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
    reqcontext['extracaption'] = extracaption
    scale_sequences = request.session['pub_scale_sequences']
    reqcontext.update(pcpt.makeScaleContext(scale_sequences, 'rnd_max'))
    return render(request, 'eyevacs/scale.html', reqcontext)

def rnd_regret(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    scale_sequences = request.session['pub_scale_sequences']
    reqcontext = pcpt.makeScaleContext(scale_sequences, 'rnd_regret')
    destination = reverse('eyevacs.views.pl_experience', args= [exp_id, pcpt_id])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
    reqcontext['extracaption'] = extracaption
    reqcontext['destination'] = destination
    return render(request, 'eyevacs/scale.html', reqcontext)

def pl_experience(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    site_vars = {'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    destination = reverse('eyevacs.views.rnd_involvement', args= [exp_id, pcpt_id])
    reqcontext['destination'] = destination
    return render (request, 'eyevacs/pl_experience.html', reqcontext)

def rnd_involvement(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    scale_sequences = request.session['pub_scale_sequences']
    reqcontext = pcpt.makeScaleContext(scale_sequences, 'rnd_involvement')
    destination = reverse('eyevacs.views.explanation_overview', args= [exp_id, pcpt_id])
    reqcontext['bt_label'] = bt_label
    reqcontext['destination'] = destination
    return render(request, 'eyevacs/scale.html', reqcontext)

def explanation_overview(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True
    destination = reverse('eyevacs.views.explanation_food', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation0_overview.html', reqcontext)

def explanation_food(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_recommend', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation1_food.html', reqcontext)

def explanation_recommend(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_distance', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation2_recommend.html', reqcontext)

def explanation_distance(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_seaview', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation3_distance.html', reqcontext)

def explanation_seaview(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_price', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation4_seaview.html', reqcontext)

def explanation_price(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_room', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation5_price.html', reqcontext)

def explanation_room(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_favattributes', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    # reqcontext['scrollable'] = True
    return render (request, 'eyevacs/explanation6_room.html', reqcontext)

def explanation_favattributes(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.explanation_ctseqintro', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation7_favattributes.html', reqcontext)

def explanation_ctseqintro(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True
    destination = reverse('eyevacs.views.decisionsequence', args= [exp_id, pcpt_id, 0])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    return render (request, 'eyevacs/explanation8_choicetasks.html', reqcontext)

########################################################################
########################################################################
########################################################################

def decisionsequence(request, exp_id, pcpt_id, ct_page):
    request.session.update(request.POST)
    request.session['timestamps'].update({request.path:datetime.utcnow()})
    #context['info'] = pcpt object erstellen!!! am besten ein dict...
    data = {}
    #just a debug variable for special purposes
    data['text'] = ''
    # data['taskcounter'] = pcpt.taskcounter
    # data['taskcounter'] = pub.taskcounter
    ctlist = request.session['pub_ctlist']
    this_task = ctlist[int(ct_page)]
    ctdict = pcpt.makeTaskDict(exp_id, this_task, int(ct_page))
    data.update(ctdict)
    rq = RequestContext(request, data)
    # if pcpt.checkNextTask(int(ct_page)):
    if int(ct_page)+1 < len(ctlist):
        next_page = int(ct_page) + 1
        destination = reverse('eyevacs.views.loadingsequence', args = [exp_id, pcpt_id, next_page])
    else:
        destination = reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id])
    data['destination'] = destination
    ########################################################################
    # lang = request.session['django_language']
    # data['language'] = 'language: '+ lang +'\n-------------\n'
    ########################################################################
    return render(request, 'eyevacs/table.html', rq)

def loadingsequence(request, exp_id, pcpt_id, ct_page):
    request.session.update(request.POST)
    request.session['timestamps'].update({request.path:datetime.utcnow()})
    request.session.modified = True
    destination = reverse('eyevacs.views.decisionsequence', args = [exp_id, pcpt_id, ct_page])

    data= {}
    data['destination'] = destination
    rq = RequestContext(request, data )

    return render(request, 'eyevacs/loading.html', rq)

def rnd_searchgoals(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    scale_sequences = request.session['pub_scale_sequences']
    reqcontext = pcpt.makeScaleContext(scale_sequences, 'rnd_searchgoals')
    destination = reverse('eyevacs.views.pl_difficulty_last', args= [exp_id, pcpt_id])
    reqcontext['bt_label'] = bt_label
    extracaption = {'left':ugettext('I do not agree at all'), 'right':ugettext('I agree very much')}
    reqcontext['extracaption'] = extracaption
    reqcontext['destination'] = destination
    return render(request, 'eyevacs/scale.html', reqcontext)

def pl_difficulty_last(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.conjoint', args= [exp_id, pcpt_id, 0])
    contextDict = pcpt.getDifficultyDict('difficulty_last')
    reqcontext = RequestContext(request, contextDict)
    extracaption = {'left':ugettext_lazy('not at all'), 'right':ugettext_lazy('very much')}
    reqcontext['extracaption'] = extracaption
    reqcontext['destination'] = destination
    reqcontext['bt_label'] = bt_label
    return render(request, 'eyevacs/pl_difficulty.html', reqcontext)

def conjoint(request, exp_id, pcpt_id, conjoint_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    conjoint = {}
    context = {}
    if int(conjoint_id) == 0:
        for i in range(0,4,1):
            conjoint[i] = pcpt.getConjoint(i)
            destination = reverse('eyevacs.views.loadingconjoint', args = [exp_id, pcpt_id])
            context['starter'] = True
    if int(conjoint_id) == 1:
        for i in range(4,8,1):
            conjoint[i-4] = pcpt.getConjoint(i)
            destination = reverse('eyevacs.views.rnd_searchgoals', args = [exp_id, pcpt_id])
            context['starter'] = False
    context['destination'] = destination
    context['bt_label'] = bt_label
    context['conjointtasks'] = conjoint
    # context['validation'] = validation
    reqcontext = RequestContext(request, context)
    return render(request, 'eyevacs/conjoint.html', reqcontext)

def loadingconjoint(request, exp_id, pcpt_id):
    '''Only in between the 2 conjoint pages.'''
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True
    destination = reverse('eyevacs.views.conjoint', args = [exp_id, pcpt_id, 1])
    data= {}
    data['destination'] = destination
    rq = RequestContext(request, data)
    return render(request, 'eyevacs/loading.html', rq)

def createUniqueKey(request):
    path = request.path
    ts_keys = request.session['timestamps'].keys()
    urls = []
    for url in ts_keys:
        if path in url:
            urls.append(url)
    counter = len(urls)
    return path + str(counter)



def rnd_happiness(request, exp_id, pcpt_id):
    pass
    # sorry happiness scale... you're out.
    # request.session.update(request.POST)
    # reqcontext = pcpt.get_scale_context('rnd_happiness')
    # destination = reverse('eyevacs.views.pl_demographics', args= [str(exp_id), str(pcpt_id)])
    # reqcontext['bt_label'] = bt_label
    # reqcontext['destination'] = destination
    # return render(request, 'eyevacs/scale.html', reqcontext)

def pl_demographics(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    destination = reverse('eyevacs.views.finalPage', args= [exp_id, pcpt_id])
    site_vars = {'destination': destination, 'bt_label':bt_label}
    reqcontext = RequestContext(request, site_vars)
    # debugpostdata(reqcontext, request.POST)
    return render (request, 'eyevacs/pl_demographics.html', reqcontext)

def finalPage(request, exp_id, pcpt_id):
    request.session.update(request.POST)
    request.session['timestamps'].update({createUniqueKey(request):datetime.utcnow()})
    request.session.modified = True

    pcpt.makeParticipant(request.session)

    # try:
    #     Thread(target=pcpt.makeParticipant, args=(request.session)).start()
    # except Exception, errtxt:
    #     print errtxt

    return render(request, 'eyevacs/thankyou.html')

    # data = {}
    # data['text'] = 'Thank You for your participation!'
    # temp_dest = reverse('eyevacs.views.', args = [exp_id, pcpt_id])
    # temp = {'destination': temp_dest}
    # temp = {'somekey': 'sometext'}
    # data['temp'] = temp
    # context = Context(data)
    # return render(request, 'eyevacs/0preview1650.html', context)

def outputCSV(request, exp_id):
    return pcpt.exportToCSV(exp_id)

def debugsaving(request):
    # pcpt.debugMakeParticipant('inc')
    # pcpt.debugMakeParticipant('bslow', )
    return render(request, 'eyevacs/thankyou.html')
#
def pcptInfo(request, exp_id, pcpt_id):
    return HttpRespones(Participant.objects.get(pk = pcpt_id))
    #return render_to_response('eyevacs/scale.html')

