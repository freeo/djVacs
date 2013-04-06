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
        templ[buybuttons[i]] = 'ctdec_'+ str(taskcounter) + '_' + str(task.amount) + '_' + str(i+1) + '_' + str(task.pk)
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

def prepareCTdecisions(full_dict):
    cts = []
    for key, value in full_dict.iteritems():
        if 'ctdec' in key:
            cts.append(key)
    ct_list = []
    for ct in cts:
        elements = ct.split('_')
        ct_dict_item = {
            'taskcounter':elements[1],
            'amount':elements[2],
            'decision':elements[3],
            'pk':elements[4]}
        ct_list.append(ct_dict_item)
    return_ct_list = sorted(ct_list, key = operator.itemgetter('taskcounter'))
    return return_ct_list
    #templ[buybuttons[i]] = str(taskcounter) + '_' + str(task.amount) + '_' + str(i+1) + '_' + str(task.pk)

def prepareCTTimestamps(raw_timestamps):
    ts = raw_timestamps
    t = timestampKeyfinder
    t1 = t('ct1', ts) - t('ct0', ts)
    t2 = t('ct2', ts) - t('ct1', ts)
    t3 = t('ct3', ts) - t('ct2', ts)
    t4 = t('ct4', ts) - t('ct3', ts)
    t5 = t('ct5', ts) - t('ct4', ts)
    t6 = t('ct6', ts) - t('ct5', ts)
    t7 = t('ct7', ts) - t('ct6', ts)
    try:
        t8  = t('ct8',ts) - t('ct7', ts)
        t9  = t('ct9', ts) - t('ct8', ts)
        t10 = t('ct10', ts) - t('ct9', ts)
        t11 = t('ct11', ts) - t('ct10', ts)
        t12 = t('ct12', ts) - t('ct11', ts)
        t13 = t('ct13', ts) - t('ct12', ts)
        t14 = t('ct14', ts) - t('ct13', ts)
        t15 = t('ct15', ts) - t('ct14', ts)
        t16 = t('conjoint/0', ts) - t('ct15', ts)
        dt_deltalist = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]
    except:
        t8 = t('ct9',ts) - t('ct8', ts)
        dt_deltalist = [t1,t2,t3,t4,t5,t6,t7,t8]
    tslist = []
    for ts in dt_deltalist:
        min_sec = str(ts.seconds / 60)+':'+str(ts.seconds % 60)
        tslist.append(min_sec)
    return tlist

def ts_url_to_string(dt_url_part_1, dt_url_part_2):
    dt1 = timestampKeyfinder(dt_url_part_1)
    dt2 = timestampKeyfinder(dt_url_part_2)
    td = dt1 - dt2
    # delta_string = str(td.seconds / 60)+':'+str(td.seconds % 60)
    delta_string = str(td.seconds)
    return delta_string

def process_transit_tstamps(raw_timestamp_dict):
    # h2totaltime = models.CharField(max_length=100)
    # h2transitdecision = models.CharField(max_length=100)
    # t_h2transitdecision = models.DateTimeField(blank = True)
    transit_ts_dict = {}
    for url, dtime in raw_timestamp_dict.iteritems():
        if 'transit/' in url:
            transit_ts_dict[url] = dtime
    ts_tuple = []
    for url, dtime in transit_ts_dict.iteritems():
        ts_tuple.append((url, dtime))
    sorted_ts_tuple = sorted(ts_tuple, key=lambda ts: ts[1])

    for i in range(0, len(sorted_ts_tuple)-1,1):
        try:
            td = sorted_ts_tuple[i+1][1] - sorted_ts_tuple[i][1]
            durationpath.append(str(td.seconds))
        except:
            pass
        searchpath.append(sorted_ts_tuple[i][0])

    return (searchpath, durationpath)

def getCT(pub, pk):
    def_group = pub.def_group
    override_group= pub.override_group
    if pub.override_group in (3,4):
        is_baseline = True
    if pub.override_group in (1,2):
        is_baseline = False
    if pub.override_group == None:
        if pub.def_group in (3,4):
            is_baseline = True
        if pub.def_group in (1,2):
            is_baseline = False

    if is_baseline:
        return External_Baseline_Choice_Task.objects.get(pk=pk)
    else:
        return External_Choice_Task.objects.get(pk=pk)

def checkCTs(pub, session_ct_ids):
    try:
        pub_cts = pub.external_choice_task_set.all()
    except:
        pub_cts = pub.external_baseline_choice_task_set.all()

    pub_ct_list =[]
    for id in pub_cts:
        pub_ct_list.append(id.pk)
    if sorted(pub_ct_list) == session_ct_ids:
        raise Exception('CTs from session and pub object don\'t match!',
            pub_ct_list,session_ct_ids)

def checkRNDs(pub, session_rnd_ids):
    pub_rnds = pub.external_order_scale_set.all()
    pub_rnd_list =[]
    for id in pub_rnds:
        pub_rnd_list.append(id.pk)
    if sorted(pub_rnd_list) == session_rnd_ids:
        raise Exception('RNDs from session and pub object don\'t match!',
            pub_rnd_list,session_rnd_ids)

def makeParticipant(s):
    '''exports whole session dictionary to pcp object.'''

    pub = s['pub']
    ts = s['timestamps']
    sorted_ctdec_list = prepareCTdecisions(s)
    ct_tslist = prepareCTTimestamps
    (transit_searchpath, transit_durationpath) = process_transit_tstamps()
    try:
        try_happiness_exist = ts_url_to_string('pl_demographics', 'rnd_happiness')
        opt_happiness = True
    except:
        opt_happiness = False
    checkCTs(pub, s['pub_ctlist_IDs'])
    checkCTs(pub, s['pub_scale_sequences_IDs'])
    rnd_dict = s['pub_scale_sequences']

    PCPT = Participant()

    PCPT.experiment = pub.experiment
    #is unique per exp, not more. grouping.group_nr[hard_id] sets condition
    PCPT.hard_id = pub.hard_id
    #inc, dec, bsl
    PCPT.def_group = pub.def_group
    PCPT.override_group= pub.override_group
    PCPT.ct_size = pub.ct_size
    #bool, real participant = False or "Test-Experiments" = True
    #maybe a switch in admin mask
    PCPT.testpcpt = s['testpcpt']
    PCPT.validated_pretest = s['validpretest']
    # begin time is pubs create_time
    PCPT.begin_time = pub.create_time
    PCPT.end_time = timestampKeyfinder('finalpage', ts)
    PCPT.total_time = str((begin_time - end_time).seconds)
    PCPT.rnd_maxQ1 = str(s['rnd_maxQ1'][0])
    PCPT.rnd_maxQ2 = str(s['rnd_maxQ2'][0])
    PCPT.rnd_maxQ3 = str(s['rnd_maxQ3'][0])
    PCPT.rnd_maxQ4 = str(s['rnd_maxQ4'][0])
    PCPT.rnd_maxQ5 = str(s['rnd_maxQ5'][0])
    PCPT.rnd_maxQ6 = str(s['rnd_maxQ6'][0])
    PCPT.t_rnd_max = ts_url_to_string('rng_regret','rnd_max')
    PCPT.rnd_regretQ1 = str(s['rnd_regretQ1'][0])
    PCPT.rnd_regretQ2 = str(s['rnd_regretQ2'][0])
    PCPT.rnd_regretQ3 = str(s['rnd_regretQ3'][0])
    PCPT.rnd_regretQ4 = str(s['rnd_regretQ4'][0])
    PCPT.rnd_regretQ5 = str(s['rnd_regretQ5'][0])
    PCPT.t_rnd_regret = ts_url_to_string('pl_experience', 'rng_regret')
    PCPT.experience_lastvacation    = str(s['experience_lastvacation'][0])
    PCPT.experience_planningvacation = str(s['experience_planningvacation'][0])
    PCPT.experience_searchduration   = str(s['experience_searchduration'][0])
    PCPT.t_experience = ts_url_to_string('rnd_involvement', 'pl_experience')
    PCPT.rnd_involvementQ1 = str(s['rnd_involvementQ1'][0])
    PCPT.rnd_involvementQ2 = str(s['rnd_involvementQ2'][0])
    PCPT.rnd_involvementQ3 = str(s['rnd_involvementQ3'][0])
    PCPT.rnd_involvementQ4 = str(s['rnd_involvementQ4'][0])
    PCPT.t_rnd_involvement = ts_url_to_string('distance', 'rnd_involvement')

    PCPT.explanation_distance = str(s['explanation_distance'][0])
    PCPT.t_expl_distance = ts_url_to_string('food', 'distance')
    PCPT.explanation_food = str(s['explanation_food'][0])
    PCPT.t_expl_food = ts_url_to_string('price', 'food')
    PCPT.explanation_price = str(s['explanation_price'][0])
    PCPT.t_expl_price = ts_url_to_string('recommend', 'price')
    PCPT.explanation_recommend = str(s['explanation_recommend'][0])
    PCPT.t_expl_recommend = ts_url_to_string('room', 'recommend')
    PCPT.explanation_room = str(s['explanation_room'][0])
    PCPT.t_expl_room = ts_url_to_string('view', 'room')
    PCPT.explanation_view = str(s['explanation_view'][0])
    PCPT.t_expl_view = ts_url_to_string('8_choicetasks', 'view')
    PCPT.fav_distance = str(s['fave_distance'][0])
    PCPT.fav_food = str(s['fav_food'][0])
    PCPT.fav_price = str(s['fav_price'][0])
    PCPT.fav_recommending = str(s['fav_recommending'][0])
    PCPT.fav_room = str(s['fav_room'][0])
    PCPT.fav_seaview = str(s['fav_seaview'][0])
    PCPT.t_expl_fav =  ts_url_to_string('ct0', '8_choicetasks')
    #the final decision
    PCPT.l = sorted_ctdec_list
    # 'taskcounter''amount''decision''pk'
    PCPT.ct1 = l[0]['decision']
    PCPT.ct2 = l[1]['decision']
    PCPT.ct3 = l[2]['decision']
    PCPT.ct4 = l[3]['decision']
    PCPT.ct5 = l[4]['decision']
    PCPT.ct6 = l[5]['decision']
    PCPT.ct7 = l[6]['decision']
    PCPT.ct8 = l[7]['decision']
    if len(l) == 16:
        PCPT.ct9  = l[9]['decision']
        ct10 = l[10]['decision']
        ct11 = l[11]['decision']
        ct12 = l[12]['decision']
        PCPT.ct13 = l[13]['decision']
        PCPT.ct14 = l[14]['decision']
        PCPT.ct15 = l[15]['decision']
        PCPT.ct16 = l[16]['decision']
    #amount of alternatives presented
    #kind of redundant, yet VERY helpful!
    PCPT.ctamount1 = l[0]['amount']
    PCPT.ctamount2 = l[1]['amount']
    PCPT.ctamount3 = l[2]['amount']
    PCPT.ctamount4 = l[3]['amount']
    PCPT.ctamount5 = l[4]['amount']
    PCPT.ctamount6 = l[5]['amount']
    PCPT.ctamount7 = l[6]['amount']
    PCPT.ctamount8 = l[7]['amount']
    if len(l) == 16:
        PCPT.ctamount9  = l[9]['amount']
        PCPT.ctamount10 = l[10]['amount']
        PCPT.ctamount11 = l[11]['amount']
        PCPT.ctamount12 = l[12]['amount']
        PCPT.ctamount13 = l[13]['amount']
        PCPT.ctamount14 = l[14]['amount']
        PCPT.ctamount15 = l[15]['amount']
        PCPT.ctamount16 = l[16]['amount']
    PCPT.cttime1 = ct_tslist[0]
    PCPT.cttime2 = ct_tslist[1]
    PCPT.cttime3 = ct_tslist[2]
    PCPT.cttime4 = ct_tslist[3]
    PCPT.cttime5 = ct_tslist[4]
    PCPT.cttime6 = ct_tslist[5]
    PCPT.cttime7 = ct_tslist[6]
    PCPT.cttime8 = ct_tslist[7]
    if len(ct_tslist) == 16:
        PCPT.cttime9 =  ct_tslist[8]
        PCPT.cttime10 = ct_tslist[9]
        PCPT.cttime11 = ct_tslist[10]
        PCPT.cttime12 = ct_tslist[11]
        PCPT.cttime13 = ct_tslist[12]
        PCPT.cttime14 = ct_tslist[13]
        PCPT.cttime15 = ct_tslist[14]
        PCPT.cttime16 = ct_tslist[15]
    PCPT.h1conjoint1 = str(s['select_con1'][0])
    PCPT.h1conjoint2 = str(s['select_con2'][0])
    PCPT.h1conjoint3 = str(s['select_con3'][0])
    PCPT.h1conjoint4 = str(s['select_con4'][0])
    PCPT.t_h1page1 = ts_url_to_string('conjoint/1', 'conjoint/0')
    PCPT.h1conjoint5 = str(s['select_con5'][0])
    PCPT.h1conjoint6 = str(s['select_con6'][0])
    PCPT.h1conjoint7 = str(s['select_con7'][0])
    PCPT.h1conjoint8 = str(s['select_con8'][0])
    PCPT.t_h1page2 = ts_url_to_string('transit/overview', 'conjoint/1')

    PCPT.h2totaltime = ts_url_to_string('transit/select', 'transit/overview')
    PCPT.h2searchpath = transit_searchpath
    PCPT.h2durationpath = transit_durationpath
    PCPT.h2transitdecision = str(s['transit'][0])
    PCPT.t_h2transitdecision = ts_url_to_string('rnd_searchgoals', 'transit/select')

    PCPT.rnd_searchgoalsQ1 = str(s['rnd_maxQ1'][0])
    PCPT.rnd_searchgoalsQ2 = str(s['rnd_maxQ2'][0])
    PCPT.rnd_searchgoalsQ3 = str(s['rnd_maxQ3'][0])
    PCPT.rnd_searchgoalsQ4 = str(s['rnd_maxQ4'][0])
    if not opt_happiness:
        PCPT.t_rnd_searchgoals = ts_url_to_string('pl_demographics', 'rnd_searchgoals')
    else:
        PCPT.t_rnd_searchgoals = ts_url_to_string('rnd_happiness', 'rnd_searchgoals')
        PCPT.rnd_happinessQ1 = str(s['rnd_happinessQ1'][0])
        PCPT.rnd_happinessQ2 = str(s['rnd_happinessQ2'][0])
        PCPT.rnd_happinessQ3 = str(s['rnd_happinessQ3'][0])
        PCPT.rnd_happinessQ4 = str(s['rnd_happinessQ4'][0])
        PCPT.t_rnd_happiness = ts_url_to_string('pl_demographics', 'rnd_happiness')

    PCPT.demo_gender = str(s['gender'][0])
    PCPT.demo_age = str(s['age'][0])
    PCPT.t_demographics = ts_url_to_string('finalPage', 'pl_demographics')

    #2nd seperate file on export
    #used initial pub data:

    # l = sorted_ctdec_list
    # getCT(pub, pk) is finds corresponding group, baseline/not
    PCPT.ct1pk = l[0]['pk']
    PCPT.ct1 = getCT(pub, ct1pk) #helper, not saved to model
    PCPT.ct1amount = ct1.amount # 2 possible ways
    PCPT.ct1a1 = ct1.a1
    PCPT.ct1a2 = ct1.a2
    PCPT.ct1a3 = ct1.a3
    PCPT.ct1a4 = ct1.a4
    PCPT.ct1a5 = ct1.a5
    PCPT.ct2pk = l[1]['pk']
    PCPT.ct2 = getCT(pub, ct2pk) #helper, not saved to model
    PCPT.ct2amount = l[1]['amount']
    PCPT.ct2a1 = ct2.a1
    PCPT.ct2a2 = ct2.a2
    PCPT.ct2a3 = ct2.a3
    PCPT.ct2a4 = ct2.a4
    PCPT.ct2a5 = ct2.a5
    PCPT.ct3pk = l[2]['pk']
    PCPT.ct3 = getCT(pub, ct3pk) #helper, not saved to model
    PCPT.ct3amount = l[2]['amount']
    PCPT.ct3a1 = ct3.a1
    PCPT.ct3a2 = ct3.a2
    PCPT.ct3a3 = ct3.a3
    PCPT.ct3a4 = ct3.a4
    PCPT.ct3a5 = ct3.a5
    PCPT.ct4pk = l[3]['pk']
    PCPT.ct4 = getCT(pub, ct4pk) #helper, not saved to model
    PCPT.ct4amount =  l[3]['amount']
    PCPT.ct4a1 = ct4.a1
    PCPT.ct4a2 = ct4.a2
    PCPT.ct4a3 = ct4.a3
    PCPT.ct4a4 = ct4.a4
    PCPT.ct4a5 = ct4.a5
    PCPT.ct5pk = l[4]['pk']
    PCPT.ct5 = getCT(pub, ct5pk) #helper, not saved to model
    PCPT.ct5amount = l[4]['amount']
    PCPT.ct5a1 = ct5.a1
    PCPT.ct5a2 = ct5.a2
    PCPT.ct5a3 = ct5.a3
    PCPT.ct5a4 = ct5.a4
    PCPT.ct5a5 = ct5.a5
    PCPT.ct6pk = l[5]['pk']
    PCPT.ct6 = getCT(pub, ct6pk) #helper, not saved to model
    PCPT.ct6amount = l[5]['amount']
    PCPT.ct6a1 = ct6.a1
    PCPT.ct6a2 = ct6.a2
    PCPT.ct6a3 = ct6.a3
    PCPT.ct6a4 = ct6.a4
    PCPT.ct6a5 = ct6.a5
    PCPT.ct7pk = l[6]['pk']
    PCPT.ct7 = getCT(pub, ct7pk) #helper, not saved to model
    PCPT.ct7amount = l[6]['amount']
    PCPT.ct7a1 = ct7.a1
    PCPT.ct7a2 = ct7.a2
    PCPT.ct7a3 = ct7.a3
    PCPT.ct7a4 = ct7.a4
    PCPT.ct7a5 = ct7.a5
    PCPT.ct8pk = l[7]['pk']
    PCPT.ct8 = getCT(pub, ct8pk) #helper, not saved to model
    PCPT.ct8amount = l[7]['amount']
    PCPT.ct8a1 = ct8.a1
    PCPT.ct8a2 = ct8.a2
    PCPT.ct8a3 = ct8.a3
    PCPT.ct8a4 = ct8.a4
    PCPT.ct8a5 = ct8.a5
    #optional CTs
    if len(l) == 16:
        PCPT.ct9pk =     l[8]['pk']
        PCPT.ct9 = getCT(pub, ct9pk) #h
        PCPT.ct9amount = ct9.amount # 2
        PCPT.ct9a1 =    ct9.a1
        PCPT.ct9a2 =    ct9.a2
        PCPT.ct9a3 =    ct9.a3
        PCPT.ct9a4 =    ct9.a4
        PCPT.ct9a5 =    ct9.a5
        PCPT.ct10pk =   l[9]['pk']
        PCPT.ct10 = getCT(pub, ct10pk) #h
        PCPT.ct10amount = l[9]['amount']
        PCPT.ct10a1 =     ct10.a1
        PCPT.ct10a2 =     ct10.a2
        PCPT.ct10a3 =     ct10.a3
        PCPT.ct10a4 =     ct10.a4
        PCPT.ct10a5 =     ct10.a5
        PCPT.ct11pk =     l[10]['pk']
        PCPT.ct11 =       getCT(pub, ct11pk)
        PCPT.ct11amount = l[10]['amount']
        PCPT.ct11a1 =     ct11.a1
        PCPT.ct11a2 =     ct11.a2
        PCPT.ct11a3 =     ct11.a3
        PCPT.ct11a4 =     ct11.a4
        PCPT.ct11a5 =     ct11.a5
        PCPT.ct12pk =     l[11]['pk']
        PCPT.ct12 =       getCT(pub, ct12pk)
        PCPT.ct12amount = l[11]['amount']
        PCPT.ct12a1 =     ct12.a1
        PCPT.ct12a2 =     ct12.a2
        PCPT.ct12a3 =     ct12.a3
        PCPT.ct12a4 =     ct12.a4
        PCPT.ct12a5 =     ct12.a5
        PCPT.ct13pk =     l[12]['pk']
        PCPT.ct13pk =     getCT(pub, ct13pk)
        PCPT.ct13amount = l[12]['amount']
        PCPT.ct13a1 =     ct13.a1
        PCPT.ct13a2 =     ct13.a2
        PCPT.ct13a3 =     ct13.a3
        PCPT.ct13a4 =     ct13.a4
        PCPT.ct13a5 =     ct13.a5
        PCPT.ct14pk =     l[13]['pk']
        PCPT.ct14 =       getCT(pub, ct14pk)
        PCPT.ct14amount = l[13]['amount']
        PCPT.ct14a1 =     ct14.a1
        PCPT.ct14a2 =     ct14.a2
        PCPT.ct14a3 =     ct14.a3
        PCPT.ct14a4 =     ct14.a4
        PCPT.ct14a5 =     ct14.a5
        PCPT.ct15pk =     l[14]['pk']
        PCPT.ct15 =       getCT(pub, ct15pk)
        PCPT.ct15amount = l[14]['amount']
        PCPT.ct15a1 =     ct15.a1
        PCPT.ct15a2 =     ct15.a2
        PCPT.ct15a3 =     ct15.a3
        PCPT.ct15a4 =     ct15.a4
        PCPT.ct15a5 =     ct15.a5
        PCPT.ct16pk =     l[15]['pk']
        PCPT.ct16 =       getCT(pub, ct16pk)
        PCPT.ct16amount = l[15]['amount']
        PCPT.ct16a1 =     ct16.a1
        PCPT.ct16a2 =     ct16.a2
        PCPT.ct16a3 =     ct16.a3
        PCPT.ct16a4 =     ct16.a4
        PCPT.ct16a5 =     ct16.a5

    #actual orders   getCT(pub, ctXpk)atCT(pub, ct8pk) #hre added up json fields to save columns
    #index: questiont = l[7]['amount'] number - Value: position
    PCPT.rnd_max_order_pk = rnd_dict['rnd_max'].pk
    PCPT.rnd_max_order =    rnd_dict['rnd_max'].scale_rnd_order_ext
    PCPT.rnd_regret_order_pk = rnd_dict['rnd_regret'].pk
    PCPT.rnd_regret_order =    rnd_dict['rnd_regret'].scale_rnd_order_ext
    PCPT.rnd_involvement_order_pk = rnd_dict['rnd_involvement'].pk
    PCPT.rnd_involvement_order =    rnd_dict['rnd_involvement'].scale_rnd_order_ext
    PCPT.rnd_searchgoals_order_pk = rnd_dict['rnd_searchgoals'].pk
    PCPT.rnd_searchgoals_order =    rnd_dict['rnd_searchgoals'].scale_rnd_order_ext
    try:
        PCPT.rnd_happiness_order_pk = rnd_dict['rnd_happiness'].pk
        PCPT.rnd_happiness_order =    rnd_dict['rnd_happiness'].scale_rnd_order_ext
    except:
        pass

    PCPT.raw_timestamps = ts
    PCPT.save()

    raise Exception('PARTICIPANT SUCCESSFUllY SAVED!!!', PCPT)



