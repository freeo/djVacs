from eyevacs.models import Scale, Scale_Question, Experiment, Participant, External_Order_Scale, Attribute, Level, Pub, External_Choice_Task
from scripts import scale_questions
import json
import re
import ast
import pdb
import operator
from django.utils.translation import ugettext
from django.forms.models import model_to_dict
from django.db import transaction
import datetime

ctsetsize = 8

#experiment specific global variables
# exp = None
# scales = None
# group_all = None
# ctasksources = None
# bsltasksources = None

#depreciated pcpt related global vars
# pcpt_id = None
# group = None
# ct_size = None #choice task size for this.pcpt.id, can vary within experiment
# scale_sequence = {}
# ctlist = []
# ctlistIDs = []
# attributes = None
# taskcounter = None
# pub = None
# pubDict = {}
# scale_order_ids = []
increasingsequence = [2,2,3,3,4,4,5,5]
decreasingsequence = [5,5,4,4,3,3,2,2]
baseline2sequence = [2,2,2,2,2,2,2,2]
baseline5sequence = [5,5,5,5,5,5,5,5]
groupName = {'1':'increasing','2':'decreasing','3':'baselinelow','4':'baselinehigh'}
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']
# session = {}
namelist = ['A','B','C','D','E','F','G','H']
max_task_size = 21
conjoint1={'id':'1','food':ugettext('good'),'recommending':'90%','distance':'1 km','view':ugettext('no sea view'),'price':ugettext('$699'),'room':ugettext('standard')}
conjoint2={'id':'2','food':ugettext('good'),'recommending':'90%','distance':'3 km','view':ugettext('full sea view'),'price':ugettext('$699'),'room':ugettext('deluxe')}
conjoint3={'id':'3','food':ugettext('excellent'),'recommending':'90%','distance':'1 km','view':ugettext('no sea view'),'price':ugettext('$899'),'room':ugettext('deluxe')}
conjoint4={'id':'4','food':ugettext('good'),'recommending':'50%','distance':'1 km','view':ugettext('full sea view'),'price':ugettext('$899'),'room':ugettext('deluxe')}
conjoint5={'id':'5','food':ugettext('excellent'),'recommending':'50%','distance':'1 km','view':ugettext('full sea view'),'price':ugettext('$699'),'room':ugettext('standard')}
conjoint6={'id':'6','food':ugettext('excellent'),'recommending':'90%','distance':'3 km','view':ugettext('full sea view'),'price':ugettext('$899'),'room':ugettext('standard')}
conjoint7={'id':'7','food':ugettext('good'),'recommending':'50%','distance':'3 km','view':ugettext('no sea view'),'price':ugettext('$899'),'room':ugettext('standard')}
conjoint8={'id':'8','food':ugettext('excellent'),'recommending':'50%','distance':'3 km','view':ugettext('no sea view'),'price':ugettext('$699'),'room':ugettext('deluxe')}
conjoint = [conjoint1,conjoint2,conjoint3,conjoint4,conjoint5,conjoint6,conjoint7,conjoint8]

def getConjoint(index):
    return conjoint[index]

def getGroup(exp_id, pcpt_id):
    exp = Experiment.objects.get(pk=exp_id)
    if pcpt_id != None:
        jsonDec = json.decoder.JSONDecoder()
        group_all = jsonDec.decode(exp.grouping.group_nr)
        groupAllocator = group_all[pcpt_id]
        return groupName[str(groupAllocator)]

def getGroupDigit(namestring):
    for key, value in groupName.iteritems():
        if value == namestring:
            return key
    else:
        raise Exception('Group digit Problem... Name-string not found')

def add_id_hole(exp_id, hole):
    exp = Experiment.objects.get(pk=exp_id)
    jsonDec = json.decoder.JSONDecoder()
    if not exp.grouping.id_holes == None:
        id_holes = jsonDec.decode(exp.grouping.id_holes)
    else:
        id_holes = []
    id_holes.append(hole)
    exp.grouping.id_holes = json.dumps(sorted(id_holes))
    exp.grouping.save()

def get_id_hole_groups(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    jsonDec = json.decoder.JSONDecoder()
    if not exp.grouping.id_holes == None:
        id_holes = jsonDec.decode(exp.grouping.id_holes)
        group_all = jsonDec.decode(exp.grouping.group_nr)
        id_hole_groups = []
        for hole in id_holes:
            hole_group = group_all[int(hole)]
            # hole_group = getGroup(group_all[int(hole)])
            id_hole_groups.append(groupName[str(hole_group)])
        return id_hole_groups
    else:
        return None

def get_next_id_hole(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    if not exp.grouping.id_holes == '[]': #only possible for == conditions
        jsonDec = json.decoder.JSONDecoder()
        id_holes = jsonDec.decode(exp.grouping.id_holes)
        return id_holes[0]
    else:
        return None

def reset_id_holes(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    if exp.pub_set.count() == 0:
        # raise Exception(exp.pub_set.count(), model_to_dict(exp), model_to_dict(exp.grouping))
        exp.grouping.id_holes = None
        exp.grouping.counter = 0
        exp.grouping.save()


def countUsedObjects(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    cts_counter = 0
    cts_parents = exp.external_source_data_set.filter(filetype='ctask')
    for parent in cts_parents:
        cts_counter += parent.external_choice_task_set.filter(used=True).count()

    scale_counter = 0
    scale_parents = exp.external_source_data_set.filter(filetype='scale')
    for parent in scale_parents:
        scale_counter += parent.external_order_scale_set.filter(used=True).count()


    bsl_counter = 0
    bsl_parents = exp.external_source_data_set.filter(filetype='bltsk')
    for parent in bsl_parents:
        bsl_counter += parent.external_baseline_choice_task_set.filter(used=True).count()

    usedDict = {'ctasks':cts_counter, 'scales':scale_counter, 'bsltsks':bsl_counter}
    return usedDict

def countUnusedObjects(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    cts_counter = 0
    cts_parents = exp.external_source_data_set.filter(filetype='ctask')
    for parent in cts_parents:
        cts_counter += parent.external_choice_task_set.filter(used=False).count()
    scale_counter = 0
    scale_parents = exp.external_source_data_set.filter(filetype='scale')
    for parent in scale_parents:
        scale_counter += parent.external_order_scale_set.filter(used=False).count()
    bsl_counter = 0
    bsl_parents = exp.external_source_data_set.filter(filetype='bltsk')
    for parent in bsl_parents:
        bsl_counter += parent.external_baseline_choice_task_set.filter(used=False).count()

    unusedDict = {'ctasks':cts_counter, 'scales':scale_counter, 'bsltsks':bsl_counter}
    return unusedDict


def infoObject(*args):
    output = ''
    if len(args) > 0:
        for arg in args:
            try:
               output += int(arg) + '\n'
            except:
               output += str(arg) + '\n'
    return output


def getScale(scales, scale_name_string):
    '''gets an External Source Data scale object.'''
    try:
        for s in scales:
            if s.header.lower() == scale_name_string.lower():
                return s
    except:
        raise Exception('Scale "%s" not found' % scale_name_string, scales)

def assignScaleOrder(exp_id, scale_name_string):
    exp = Experiment.objects.get(pk=exp_id)
    scales = exp.external_source_data_set.filter(filetype = 'scale')
    current_scale = getScale(scales, scale_name_string)
    try:
        assign_this_scale = current_scale.external_order_scale_set.order_by("used", "pk")[0]
        assign_this_scale.used = True
        assign_this_scale.save()
        # ordered = current_scale.external_order_scale_set.order_by("pk")
        # assign_this_scale = ordered.filter(linked_pcpt=None)[0]
    except:
        raise Exception('We ran out of '+scale_name_string+' orderings! Quick! We need more!')
    return assign_this_scale
#
# def incrementTaskCounter(pub):
#     # global taskcounter
#     # taskcounter += 1
#     pub.taskcounter += 1
#     pub.save()
#
def createBaselineTasklist(pub, condition ):
    # global ctlist
    # global ctlistIDs
    cts = []
    exp_id = pub.experiment.pk
    ct_size = pub.ct_size
    #a set consists of 8(ctsetsize) tasks
    ctset = (ct_size / ctsetsize)
    if condition == 'baselinelow':
        amount = baseline2sequence[0] #just pick first, all the same
        sequence = baseline2sequence
        bsl_source_file = getBSLTaskSource(exp_id, amount)
    elif condition == 'baselinehigh':
        amount = baseline5sequence[0]
        sequence = baseline5sequence
        bsl_source_file = getBSLTaskSource(exp_id, amount)
    sequence_length = ctset * len(sequence)

    #get bsl by hard id, set linked pcpt of id x after save()
    free_bsl_id = bsl_source_file.external_baseline_choice_task_set.order_by('used','pk')[0].id_hard
    #order_by could be way more complicated, but the implications of ascending order in the source file make this obsolete. This naive approach should work.
    # the first set consists of the full 21 max tasks, because all have to be set to 'used'
    # bslCTs = bsl_source_file.external_baseline_choice_task_set.order_by('used','pk')[0:21]
    bslCTs = bsl_source_file.external_baseline_choice_task_set.filter(id_hard = free_bsl_id).order_by('pk')
    # raise Exception(len(bslCTs))
    with transaction.commit_on_success():
        for ct in bslCTs:
            ct.used = True
            ct.save()
    #debug
    howlong  = len(bslCTs)

    return bslCTs[0:sequence_length]
    # ctlist = bslCTs[0:sequence_length]

    #debug purposes
    # for ct in ctlist:
        # ctlistIDs.append(ct.pk)

    # notFound = 1
    # while notFound:
    #     i = 0
    #     if bslCTs[i].linked_pcpt == None:
    #         bsl_id = bslCTs[i].id_hard
    #         notFound = 0
    #         break
    #     else:
    #         if i < len(bslCTs):
    #             i += 1
    #         else:
    #             print 'no free baseline choice tasks left... must be a bug.'
    #             notFound = 0
    #             break
    # bsl_tasks = bslCTs.filter(id_hard = bsl_id)
    # #exp.External_Baseline_Choice_Task.objects.filter(id_hard = bsl_id)
    # ct_bsl_list = [None]*max_task_size
    # for i in range(0,len(bsl_tasks),1):
    #     ctlist_index = bsl_tasks[i].task-1
    #     ct_bsl_list[ctlist_index] = bsl_tasks[i]
    # return ct_bsl_list

def setCTaskSources(exp_id):
    ''' Makes a list of CTask source files with index = amount.'''
    exp = Experiment.objects.get(pk=exp_id)
    all_sources = exp.external_source_data_set.filter(filetype = 'ctask')
    length = len(all_sources)
    ctasksources = [None]*len(all_sources)
    for i in all_sources:
        #amount begins with 2!!!
        index = i.external_choice_task_set.all()[0].amount -2
        ctasksources[index] = i
    # Same for baseline source files
    all_sources = exp.external_source_data_set.filter(filetype = 'bltsk')
    bsltasksources = []
    for i in all_sources:
        bsltasksources.append(i)
    return (ctasksources, bsltasksources)

def getCTaskSource(exp_id, get_amount):
    (ctasksources, bsltasksources) = setCTaskSources(exp_id)
    return ctasksources[get_amount -2]

def getBSLTaskSource(exp_id, get_amount):
    (ctasksources, bsltasksources) = setCTaskSources(exp_id)
    for bsl in bsltasksources:
        first_element = bsl.external_baseline_choice_task_set.all()[0]
        if first_element.amount == get_amount:
            return bsl
    else:
        raise Exception("We lack a BSL Source file.")


def getFreeCT(pub, get_amount):
    amount_source = getCTaskSource(pub.experiment.pk, get_amount)
    try:
        #the opposite of "used" is "-used" ! "+used" is invalid in bools.
        assign_this_ct = amount_source.external_choice_task_set.order_by("used", "pk")[0]
        assign_this_ct.used = True
        assign_this_ct.save()
    except:
        raise Exception('We ran out of '+amount+' choice tasks! Quick! We need more!')
    #write USED before return
    return assign_this_ct

# def createTasklist(condition, ct_size):
def createTasklist(pub, group):
    cts = []
    #a set consists of 8(ctsetsize) tasks
    ct_size = pub.ct_size
    ctset = (ct_size / ctsetsize)
    if group == 'increasing':
        sequence = increasingsequence
    elif group == 'decreasing':
        sequence = decreasingsequence
    # amount_list = range(2,9,1)
    for s in range(0,ctset,1):
        # for a in amount_list:
        for a in sequence:
            cts.append(getFreeCT(pub, a))
    #return:
    return cts

def orderTasklist(ctlist, rule):
    #operator order by key
    # amount_list = [2:8]
    if rule == 'increasing':
         law_order_temp = sorted(ctlist, key=operator.attrgetter('amount'))
         law_order = sorted(law_order_temp, key=operator.attrgetter('pk'))
         final_list = law_order
    if rule == 'decreasing':
         law_order_temp = sorted(ctlist, key=operator.attrgetter('pk'))
         law_order = sorted(law_order_temp, key=operator.attrgetter('amount'), reverse=True)
         final_list = law_order
         # pdb.set_trace()
    return final_list

def setChoiceTasks(pub):
    # pub.taskcounter = 0 #set as default in model
    # pdb.set_trace()
    # defines (pub.)CTLIST
    if pub.override_group == None:
        group_nr = pub.def_group
    else:
        group_nr = pub.override_group
    group = groupName[group_nr]
    if group == 'baselinelow':
        ctlist = createBaselineTasklist(pub, group)
    if group == 'baselinehigh':
        ctlist = createBaselineTasklist(pub, group)
    if group == 'increasing':
        ctlist = createTasklist(pub, group)
        ctlist = orderTasklist(ctlist, group)
    if group == 'decreasing':
        ctlist = createTasklist(pub, group)
        ctlist = orderTasklist(ctlist, group)
    return ctlist

def getAttributeLabelDict(exp_id):
    exp = Experiment.objects.get(pk=exp_id)
    attributes = exp.attribute_set.all()
    #rc11 is always empty
    attribute_keys = ['rc21', 'rc31', 'rc41', 'rc51', 'rc61', 'rc71', 'rc81']
    attribute_values = [None]*len(attributes)
    temp = {}
    for a in attributes:
        attribute_values[a.position -1] = a.name
    for i in range (0, len(attribute_values),1):
        temp[attribute_keys[i]] = attribute_values[i]
    return temp

# def checkNextTask(curr_page):
#     if curr_page+1 < len(ctlist):
#         return True
#     else:
#         return False

def checkNextConjoint(curr_conjoint):
    if curr_conjoint+1 < len(conjoint):
        return True
    else:
        return False

# def getTask(task_nr):
def makeTaskDict(exp_id, ctask, taskcounter):
    #maps a choice task to template: table.html
    #cells of attributes: can wait...
    # attr = ctlist
    templ = {}
    # task = ctlist[task_nr]
    task = ctask
    a1keys = ['rc12', 'rc22', 'rc32', 'rc42', 'rc52', 'rc62', 'rc72' ]
    a2keys = ['rc13', 'rc23', 'rc33', 'rc43', 'rc53', 'rc63', 'rc73' ]
    a3keys = ['rc14', 'rc24', 'rc34', 'rc44', 'rc54', 'rc64', 'rc74' ]
    a4keys = ['rc15', 'rc25', 'rc35', 'rc45', 'rc55', 'rc65', 'rc75' ]
    a5keys = ['rc16', 'rc26', 'rc36', 'rc46', 'rc56', 'rc66', 'rc76' ]
    a6keys = ['rc17', 'rc27', 'rc37', 'rc47', 'rc57', 'rc67', 'rc77' ]
    a7keys = ['rc18', 'rc28', 'rc38', 'rc48', 'rc58', 'rc68', 'rc78' ]
    a8keys = ['rc19', 'rc29', 'rc39', 'rc49', 'rc59', 'rc69', 'rc79' ]
    buybuttons = ['rc82', 'rc83', 'rc84', 'rc85', 'rc86', 'rc87', 'rc88', 'rc89']
    alts = []
    alts.append(a1keys)
    alts.append(a2keys)
    alts.append(a3keys)
    alts.append(a4keys)
    alts.append(a5keys)
    alts.append(a6keys)
    alts.append(a7keys)
    alts.append(a8keys)
    #old version, max 8 alternatives
    # altModel = [task.a1, task.a2, task.a3, task.a4, task.a5, task.a6,task.a7, task.a8]
    altModel = [task.a1, task.a2, task.a3, task.a4, task.a5]
    for i in range(0, task.amount, 1):
        templ.update(mapCT(exp_id, alts[i], altModel[i], i))
        #taskbysequenceviewn_amountofalternatives_choosenalternative_taskuniquepk
        templ[buybuttons[i]] = str(taskcounter) + '_' + str(task.amount) + '_' + str(i+1) + '_' + str(task.pk)
    templ.update(getAttributeLabelDict(exp_id))
    #finalize:
    return templ

def mapCT(exp_id, dictKeys, rawvalues, nameindex):
    #prepare raw values
    optionSTR = ast.literal_eval(rawvalues)
    option = [int(x) for x in optionSTR]
    temp = {}
    #Option Header in table
    temp[dictKeys[0]] = 'Option '+ mapNameindex(nameindex)
    #uses +1 offset for header of alternative: 'a1'
    for j in range(1, len(option) +1, 1):
        temp[dictKeys[j]] = mapAttrLevel(exp_id, option[j-1]-1, j)
    return temp

def mapNameindex(nameindex):
    return namelist[nameindex]

def mapAttrLevel(exp_id, lvlvalue, attrposition):
    exp = Experiment.objects.get(pk=exp_id)
    attributes = exp.attribute_set.all()
    a = attributes.get(position = attrposition)
    output = a.level_set.get(value = lvlvalue).name
    return output

# def initExp(exp_id):
    # global exp
    # global scales
    # global group_all
    # exp = Experiment.objects.get(pk = exp_id)

    # setCTaskSources()
    # scales = exp.external_source_data_set.filter(filetype = 'scale')
    # jsonDec = json.decoder.JSONDecoder()
    # group_all = jsonDec.decode(exp.grouping.group_nr)
    # global attributes
    # attributes = exp.attribute_set.all()


def initPcpt(exp_id, ext_ct_size, ext_sessionid, ext_csrftoken, condition):
    '''Initiates a participant stub (pub).'''
    # global scale_sequence
    # global scale_order_ids
    # global id_hole_used
    exp = Experiment.objects.get(pk=exp_id)
    #plain, simple, hard:
    #wait, wait, wait... forgot the id_holes!
    # if not exp.grouping.id_holes in ('[]', None): #only possible for == conditions
    if exp.grouping.id_holes != '[]': #only possible for == conditions
        jsonDec = json.decoder.JSONDecoder()
        id_holes = jsonDec.decode(exp.grouping.id_holes)
        hole_to_fill = id_holes[0] #first in, first out
        pcpt_id = hole_to_fill
        del id_holes[0]
        exp.grouping.id_holes = json.dumps(id_holes)
        exp.grouping.save()
        id_hole_used = True
    else:
        pcpt_id = exp.grouping.counter
        id_hole_used = False

    group = getGroup(exp_id, pcpt_id)
    ########################################################################
    #move to legacy?!
    # if (ext_pcpt_id == None): #should better be not used, too much confusion
        # has to be increased after pcpt.save() !!!
        # pcpt_id = exp.grouping.counter
    ########################################################################

    # manual override
    # raise Exception(condition)
    if condition == 'increasing':
        group = 'increasing'
    if condition == 'decreasing':
        group = 'decreasing'
    if condition == 'baselinelow':
        group = 'baselinelow'
    if condition == 'baselinehigh':
        group = 'baselinehigh'

    # rnd scale orderings
    scale_sequence = {}
    for scale in scale_names:
        scale_sequence[scale] = assignScaleOrder(exp_id, scale)

    # debug purposes:
    # for name, scale_object in scale_sequence.iteritems():
        # scale_order_ids.append(scale_object.pk)

    # return infoObject(exp.grouping.counter, group, scale_sequence)

    #Save all to pub. Needed to mark files as "used"
    pub = Pub()
    pub.experiment = exp
    pub.ct_size = ext_ct_size
    pub.hard_id = pcpt_id
    pub.sessionid = ext_sessionid
    pub.csrftoken = ext_csrftoken
    # pub.hard_id = exp.grouping.counter
    if condition == '':
        pub.def_group = getGroupDigit(group)
    else:
        pub.def_group = getGroupDigit(getGroup(exp_id, pcpt_id))
        pub.override_group = getGroupDigit(group)

    #tag: write database
    pub.save()

    #here's the cheese
    ctlist = setChoiceTasks(pub)

    with transaction.commit_on_success():
        for ct in ctlist:
            ct.linked_pub = pub
            ct.save()
        for name, scale_object in scale_sequence.iteritems():
            scale_object.linked_pub = pub
            scale_object.save()
        #tag: Increase Grouping Next Pub/PCPT
        if not id_hole_used:
            exp.grouping.counter += 1
            exp.grouping.save()

    # pubDict[pcpt_id] = pub
    return pcpt_id, ctlist, pub, scale_sequence

def makeScaleContext(scale_sequence, scale_name_string):
    question_title = scale_questions.question_titles[scale_name_string]
    scale_name = scale_name_string
    order_id = scale_sequence[scale_name_string].pk
    question_order = map(int, External_Order_Scale.objects.get(pk=order_id).scale_rnd_order_ext.split(','))
    questions = []
    restoreCheck = [None]*7
    for i in range(0, len(question_order),1):
        qtext = scale_questions.questions[scale_name_string][question_order[i]-1]
        qcaption= scale_questions.question_captions[scale_name_string][question_order[i]-1]
        qid = question_order[i]
        q = {'text':qtext,'id':qid, 'caption':qcaption}
        questions.append(q)
    # lb_button_continue = 'Continue'
    context = {'question_title': question_title,'scale_name':scale_name, 'questions':questions , 'restoreCheck':restoreCheck}
    return context

def timestampKeyfinder(urlstring, timestamps):
    '''urlstring is the last part of the url, timestamps is the dict.'''
    for key, value in timestamps.iteritems():
        if urlstring.lower() in key.lower():
            return value

def ctDissect(ctstr):
    elements = ctstr.split('_')
    return {
        'taskcounter':elements[0],
        'amount':elements[1],
        'decision':elements[2],
        'pk':elements[3]
    }
    #templ[buybuttons[i]] = str(taskcounter) + '_' + str(task.amount) + '_' + str(i+1) + '_' + str(task.pk)

def makeParticipant(s):
    '''exports whole session dictionary to pcp object.'''

    pub = s['pub']
    ts = s['timestamps']
    s['']
    experiment = pub.experiment
    #is unique per exp, not more. grouping.group_nr[hard_id] sets condition
    hard_id = pub.hard_id
    #inc, dec, bsl
    def_group = pub.def_group
    override_group= pub.override_group
    ct_size = pub.ct_size
    #bool, real participant = False or "Test-Experiments" = True
    #maybe a switch in admin mask
    testpcpt = s['testpcpt']
    validated_pretest = s['validpretest']
    # begin time is pubs create_time
    begin_time = pub.create_time
    end_time = timestampKeyfinder('finalpage', ts)
    rnd_maxQ1 = str(s['rnd_maxQ1'][0])
    rnd_maxQ2 = str(s['rnd_maxQ2'][0])
    rnd_maxQ3 = str(s['rnd_maxQ3'][0])
    rnd_maxQ4 = str(s['rnd_maxQ4'][0])
    rnd_maxQ5 = str(s['rnd_maxQ5'][0])
    rnd_maxQ6 = str(s['rnd_maxQ6'][0])
    t_rnd_max = timestampKeyfinder('rnd_max', ts)
    rnd_regretQ1 = str(s['rnd_regretQ1'][0])
    rnd_regretQ2 = str(s['rnd_regretQ2'][0])
    rnd_regretQ3 = str(s['rnd_regretQ3'][0])
    rnd_regretQ4 = str(s['rnd_regretQ4'][0])
    rnd_regretQ5 = str(s['rnd_regretQ5'][0])
    t_rnd_regret = timestampKeyfinder('rng_regret', ts)
    experience_lastvacation     = str(s['experience_lastvacation'][0])
    experience_planningvacation = str(s['experience_planningvacation'][0])
    experience_searchduration   = str(s['experience_searchduration'][0])
    t_experience = timestampKeyfinder('pl_experience', ts)
    rnd_involvementQ1 = str(s['rnd_involvementQ1'][0])
    rnd_involvementQ2 = str(s['rnd_involvementQ2'][0])
    rnd_involvementQ3 = str(s['rnd_involvementQ3'][0])
    rnd_involvementQ4 = str(s['rnd_involvementQ4'][0])
    t_rnd_involvement = timestampKeyfinder('rnd_involvement', ts)

    explanation_distance = str(s['explanation_distance'][0])
    t_expl_distance = timestampKeyfinder('distance', ts)
    explanation_food = str(s['explanation_food'][0])
    t_expl_food = timestampKeyfinder('food', ts)
    explanation_price = str(s['explanation_price'][0])
    t_expl_price = timestampKeyfinder('price', ts)
    explanation_recommend = str(s['explanation_recommend'][0])
    t_expl_recommend = timestampKeyfinder('recommend', ts)
    explanation_room = str(s['explanation_room'][0])
    t_expl_room =  timestampKeyfinder('room', ts)
    explanation_view = str(s['explanation_view'][0])
    t_expl_view = timestampKeyfinder('view', ts)
    fav_distance = str(s['fave_distance'][0])
    fav_food = str(s['fav_food'][0])
    fav_price = str(s['fav_price'][0])
    fav_recommending = str(s['fav_recommending'][0])
    fav_room = str(s['fav_room'][0])
    fav_seaview = str(s['fav_seaview'][0])
    t_expl_fav = timestampKeyfinder('8_choicetasks', ts)
    #the final decision
    ct1 =
    ct2 = models.CharField(max_length=100)
    ct3 = models.CharField(max_length=100)
    ct4 = models.CharField(max_length=100)
    ct5 = models.CharField(max_length=100)
    ct6 = models.CharField(max_length=100)
    ct7 = models.CharField(max_length=100)
    ct8 = models.CharField(max_length=100)
    ct9 = models.CharField(max_length=100, null = True, blank = True)
    ct10 = models.CharField(max_length=100, null = True, blank = True)
    ct11 = models.CharField(max_length=100, null = True, blank = True)
    ct12 = models.CharField(max_length=100, null = True, blank = True)
    ct13 = models.CharField(max_length=100, null = True, blank = True)
    ct14 = models.CharField(max_length=100, null = True, blank = True)
    ct15 = models.CharField(max_length=100, null = True, blank = True)
    ct16 = models.CharField(max_length=100, null = True, blank = True)
    #amount of alternatives presented
    #kind of redundant, yet VERY helpful!
    ctamount1 = models.CharField(max_length=100)
    ctamount2 = models.CharField(max_length=100)
    ctamount3 = models.CharField(max_length=100)
    ctamount4 = models.CharField(max_length=100)
    ctamount5 = models.CharField(max_length=100)
    ctamount6 = models.CharField(max_length=100)
    ctamount7 = models.CharField(max_length=100)
    ctamount8 = models.CharField(max_length=100)
    ctamount9 = models.CharField(max_length=100, null = True, blank = True)
    ctamount10 = models.CharField(max_length=100, null = True, blank = True)
    ctamount11 = models.CharField(max_length=100, null = True, blank = True)
    ctamount12 = models.CharField(max_length=100, null = True, blank = True)
    ctamount13 = models.CharField(max_length=100, null = True, blank = True)
    ctamount14 = models.CharField(max_length=100, null = True, blank = True)
    ctamount15 = models.CharField(max_length=100, null = True, blank = True)
    ctamount16 = models.CharField(max_length=100, null = True, blank = True)
    cttime1 = models.CharField(max_length=100)
    cttime2 = models.CharField(max_length=100)
    cttime3 = models.CharField(max_length=100)
    cttime4 = models.CharField(max_length=100)
    cttime5 = models.CharField(max_length=100)
    cttime6 = models.CharField(max_length=100)
    cttime7 = models.CharField(max_length=100)
    cttime8 = models.CharField(max_length=100)
    cttime9 = models.CharField(max_length=100, null = True, blank = True)
    cttime10 = models.CharField(max_length=100, null = True, blank = True)
    cttime11 = models.CharField(max_length=100, null = True, blank = True)
    cttime12 = models.CharField(max_length=100, null = True, blank = True)
    cttime13 = models.CharField(max_length=100, null = True, blank = True)
    cttime14 = models.CharField(max_length=100, null = True, blank = True)
    cttime15 = models.CharField(max_length=100, null = True, blank = True)
    cttime16 = models.CharField(max_length=100, null = True, blank = True)
    h1conjoint1 = models.CharField(max_length=100)
    h1conjoint2 = models.CharField(max_length=100)
    h1conjoint3 = models.CharField(max_length=100)
    h1conjoint4 = models.CharField(max_length=100)
    t_h1page1 = models.DateTimeField(blank = True)
    h1conjoint5 = models.CharField(max_length=100)
    h1conjoint6 = models.CharField(max_length=100)
    h1conjoint7 = models.CharField(max_length=100)
    h1conjoint8 = models.CharField(max_length=100)
    t_h1page2 = models.DateTimeField(blank = True)

    h2totaltime = models.CharField(max_length=100)
    h2searchpath = models.TextField()
    h2durationpath = models.TextField()
    h2transitdecision = models.CharField(max_length=100)
    t_h2transitdecision = models.DateTimeField(blank = True)

    rnd_searchgoalsQ1 = models.IntegerField()
    rnd_searchgoalsQ2 = models.IntegerField()
    rnd_searchgoalsQ3 = models.IntegerField()
    rnd_searchgoalsQ4 = models.IntegerField()
    t_rnd_searchgoals = models.DateTimeField(blank = True)
    #OPTIONAL EXPORT
    rnd_happinessQ1 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ2 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ3 = models.IntegerField(max_length=100, null = True, blank = True)
    rnd_happinessQ4 = models.IntegerField(max_length=100, null = True, blank = True)
    t_rnd_happiness = models.DateTimeField(blank = True)

    demo_gender = models.CharField(max_length=6, choices= GENDER_CHOICES)
    demo_age = models.IntegerField()
    t_demographics = models.DateTimeField(blank = True)

    #2nd seperate file on export
    #used initial pub data:
    ct1pk = models.CharField(max_length=100)
    ct1amount = models.CharField(max_length=100)
    ct1a1 = models.CharField(max_length=100)
    ct1a2 = models.CharField(max_length=100)
    ct1a3 = models.CharField(max_length=100)
    ct1a4 = models.CharField(max_length=100)
    ct1a5 = models.CharField(max_length=100)
    ct2pk = models.CharField(max_length=100)
    ct2amount = models.CharField(max_length=100)
    ct2a1 = models.CharField(max_length=100)
    ct2a2 = models.CharField(max_length=100)
    ct2a3 = models.CharField(max_length=100)
    ct2a4 = models.CharField(max_length=100)
    ct2a5 = models.CharField(max_length=100)
    ct3pk = models.CharField(max_length=100)
    ct3amount = models.CharField(max_length=100)
    ct3a1 = models.CharField(max_length=100)
    ct3a2 = models.CharField(max_length=100)
    ct3a3 = models.CharField(max_length=100)
    ct3a4 = models.CharField(max_length=100)
    ct3a5 = models.CharField(max_length=100)
    ct4pk = models.CharField(max_length=100)
    ct4amount = models.CharField(max_length=100)
    ct4a1 = models.CharField(max_length=100)
    ct4a2 = models.CharField(max_length=100)
    ct4a3 = models.CharField(max_length=100)
    ct4a4 = models.CharField(max_length=100)
    ct4a5 = models.CharField(max_length=100)
    ct5pk = models.CharField(max_length=100)
    ct5amount = models.CharField(max_length=100)
    ct5a1 = models.CharField(max_length=100)
    ct5a2 = models.CharField(max_length=100)
    ct5a3 = models.CharField(max_length=100)
    ct5a4 = models.CharField(max_length=100)
    ct5a5 = models.CharField(max_length=100)
    ct6pk = models.CharField(max_length=100)
    ct6amount = models.CharField(max_length=100)
    ct6a1 = models.CharField(max_length=100)
    ct6a2 = models.CharField(max_length=100)
    ct6a3 = models.CharField(max_length=100)
    ct6a4 = models.CharField(max_length=100)
    ct6a5 = models.CharField(max_length=100)
    ct7pk = models.CharField(max_length=100)
    ct7amount = models.CharField(max_length=100)
    ct7a1 = models.CharField(max_length=100)
    ct7a2 = models.CharField(max_length=100)
    ct7a3 = models.CharField(max_length=100)
    ct7a4 = models.CharField(max_length=100)
    ct7a5 = models.CharField(max_length=100)
    ct8pk = models.CharField(max_length=100)
    ct8amount = models.CharField(max_length=100)
    ct8a1 = models.CharField(max_length=100)
    ct8a2 = models.CharField(max_length=100)
    ct8a3 = models.CharField(max_length=100)
    ct8a4 = models.CharField(max_length=100)
    ct8a5 = models.CharField(max_length=100)
    #optional CTs
    ct9pk = models.CharField(max_length=100, null = True, blank = True)
    ct9amount = models.CharField(max_length=100, null = True, blank = True)
    ct9a1 = models.CharField(max_length=100, null = True, blank = True)
    ct9a2 = models.CharField(max_length=100, null = True, blank = True)
    ct9a3 = models.CharField(max_length=100, null = True, blank = True)
    ct9a4 = models.CharField(max_length=100, null = True, blank = True)
    ct9a5 = models.CharField(max_length=100, null = True, blank = True)
    ct10pk = models.CharField(max_length=100, null = True, blank = True)
    ct10amount = models.CharField(max_length=100, null = True, blank = True)
    ct10a1 = models.CharField(max_length=100, null = True, blank = True)
    ct10a2 = models.CharField(max_length=100, null = True, blank = True)
    ct10a3 = models.CharField(max_length=100, null = True, blank = True)
    ct10a4 = models.CharField(max_length=100, null = True, blank = True)
    ct10a5 = models.CharField(max_length=100, null = True, blank = True)
    ct11pk = models.CharField(max_length=100, null = True, blank = True)
    ct11amount = models.CharField(max_length=100, null = True, blank = True)
    ct11a1 = models.CharField(max_length=100, null = True, blank = True)
    ct11a2 = models.CharField(max_length=100, null = True, blank = True)
    ct11a3 = models.CharField(max_length=100, null = True, blank = True)
    ct11a4 = models.CharField(max_length=100, null = True, blank = True)
    ct11a5 = models.CharField(max_length=100, null = True, blank = True)
    ct12pk = models.CharField(max_length=100, null = True, blank = True)
    ct12amount = models.CharField(max_length=100, null = True, blank = True)
    ct12a1 = models.CharField(max_length=100, null = True, blank = True)
    ct12a2 = models.CharField(max_length=100, null = True, blank = True)
    ct12a3 = models.CharField(max_length=100, null = True, blank = True)
    ct12a4 = models.CharField(max_length=100, null = True, blank = True)
    ct12a5 = models.CharField(max_length=100, null = True, blank = True)
    ct13pk = models.CharField(max_length=100, null = True, blank = True)
    ct13amount = models.CharField(max_length=100, null = True, blank = True)
    ct13a1 = models.CharField(max_length=100, null = True, blank = True)
    ct13a2 = models.CharField(max_length=100, null = True, blank = True)
    ct13a3 = models.CharField(max_length=100, null = True, blank = True)
    ct13a4 = models.CharField(max_length=100, null = True, blank = True)
    ct13a5 = models.CharField(max_length=100, null = True, blank = True)
    ct14pk = models.CharField(max_length=100, null = True, blank = True)
    ct14amount = models.CharField(max_length=100, null = True, blank = True)
    ct14a1 = models.CharField(max_length=100, null = True, blank = True)
    ct14a2 = models.CharField(max_length=100, null = True, blank = True)
    ct14a3 = models.CharField(max_length=100, null = True, blank = True)
    ct14a4 = models.CharField(max_length=100, null = True, blank = True)
    ct14a5 = models.CharField(max_length=100, null = True, blank = True)
    ct15pk = models.CharField(max_length=100, null = True, blank = True)
    ct15amount = models.CharField(max_length=100, null = True, blank = True)
    ct15a1 = models.CharField(max_length=100, null = True, blank = True)
    ct15a2 = models.CharField(max_length=100, null = True, blank = True)
    ct15a3 = models.CharField(max_length=100, null = True, blank = True)
    ct15a4 = models.CharField(max_length=100, null = True, blank = True)
    ct15a5 = models.CharField(max_length=100, null = True, blank = True)
    ct16pk = models.CharField(max_length=100, null = True, blank = True)
    ct16amount = models.CharField(max_length=100, null = True, blank = True)
    ct16a1 = models.CharField(max_length=100, null = True, blank = True)
    ct16a2 = models.CharField(max_length=100, null = True, blank = True)
    ct16a3 = models.CharField(max_length=100, null = True, blank = True)
    ct16a4 = models.CharField(max_length=100, null = True, blank = True)
    ct16a5 = models.CharField(max_length=100, null = True, blank = True)

    #actual orders are added up json fields to save columns
    #index: question number - Value: position
    rnd_max_order_pk = models.CharField(max_length=100)
    rnd_max_order = models.TextField()
    rnd_regret_order_pk = models.CharField(max_length=100)
    rnd_regret_order = models.TextField()
    rnd_involvement_order_pk = models.CharField(max_length=100)
    rnd_involvement_order = models.TextField()
    rnd_searchgoals_order_pk = models.CharField(max_length=100)
    rnd_searchgoals_order = models.TextField()
    rnd_happiness_order_pk = models.CharField(max_length=100, null = True, blank = True)
    rnd_happiness_order = models.TextField(max_length=100, null = True, blank = True)


