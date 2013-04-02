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

ctsetsize = 8

exp = None
scales = None
# pcpt_id = None
group = None
group_all = None
ct_size = None #choice task size for this.pcpt.id, can vary within experiment
ctasksources = None
bsltasksources = None
ctlist = []
ctlistIDs = []
attributes = None
taskcounter = None
# pub = None
pubDict = {}
increasingsequence = [2,2,3,3,4,4,5,5]
decreasingsequence = [5,5,4,4,3,3,2,2]
baseline2sequence = [2,2,2,2,2,2,2,2]
baseline5sequence = [5,5,5,5,5,5,5,5]
groupName = {'1':'increasing','2':'decreasing','3':'baselinelow','4':'baselinehigh'}
scale_sequence = {}
scale_order_ids = []
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

def getGroup(this_id):
    if this_id != None:
        jsonDec = json.decoder.JSONDecoder()
        group_all = jsonDec.decode(exp.grouping.group_nr)
        groupAllocator = group_all[this_id]
        return groupName[str(groupAllocator)]

def getGroupDigit(namestring):
    for key, value in groupName.iteritems():
        if value == namestring:
            return key
    else:
        raise Exception('Group digit Problem... Name-string not found')

def add_id_hole(hole):
    jsonDec = json.decoder.JSONDecoder()
    if not exp.grouping.id_holes == None:
        id_holes = jsonDec.decode(exp.grouping.id_holes)
    else:
        id_holes = []
    id_holes.append(hole)
    exp.grouping.id_holes = json.dumps(sorted(id_holes))
    exp.grouping.save()

def get_id_hole_groups():
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

def get_next_id_hole():
    if not exp.grouping.id_holes == '[]': #only possible for == conditions
        jsonDec = json.decoder.JSONDecoder()
        id_holes = jsonDec.decode(exp.grouping.id_holes)
        return id_holes[0]
    else:
        return None

def reset_id_holes():
    if exp.pub_set.count() == 0:
        # raise Exception(exp.pub_set.count(), model_to_dict(exp), model_to_dict(exp.grouping))
        exp.grouping.id_holes = None
        exp.grouping.counter = 0
        exp.grouping.save()


def countUsedObjects():

    cts_counter = 0
    cts_parents = exp.external_source_data_set.filter(filetype='ctask')
    for parent in cts_parents:
        cts_counter += parent.external_choice_task_set.filter(used='True').count()

    scale_counter = 0
    scale_parents = exp.external_source_data_set.filter(filetype='scale')
    for parent in scale_parents:
        scale_counter += parent.external_order_scale_set.filter(used='True').count()


    bsl_counter = 0
    bsl_parents = exp.external_source_data_set.filter(filetype='bltsk')
    for parent in bsl_parents:
        bsl_counter += parent.external_baseline_choice_task_set.filter(used='True').count()

    usedDict = {'ctasks':cts_counter, 'scales':scale_counter, 'bsltsks':bsl_counter}
    return usedDict


def infoObject(*args):
    output = ''
    if len(args) > 0:
        for arg in args:
            try:
               output += int(arg) + '\n'
            except:
               output += str(arg) + '\n'
    return output


def getScale(scale_name_string):
    '''gets an External Source Data scale object.'''
    try:
        for s in scales:
            if s.header.lower() == scale_name_string.lower():
                return s
    except:
        raise Exception('Scale "%s" not found' % scale_name_string, scales)

# def parseHtml(text):
#     html = re.sub(r'\n', '<br>', text)
#     return html

def assignScaleOrder(scale_name_string):
    current_scale = getScale(scale_name_string)
    try:
        assign_this_scale = current_scale.external_order_scale_set.order_by("used", "pk")[0]
        assign_this_scale.used = True
        assign_this_scale.save()
        # ordered = current_scale.external_order_scale_set.order_by("pk")
        # assign_this_scale = ordered.filter(linked_pcpt=None)[0]
    except:
        raise Exception('We ran out of '+scale_name_string+' orderings! Quick! We need more!')
    return assign_this_scale

def incrementTaskCounter():
    global taskcounter
    taskcounter += 1

def createBaselineTasklist(condition):
    global ctlist
    global ctlistIDs
    cts = []
    #a set consists of 8(ctsetsize) tasks
    ctset = (ct_size / ctsetsize)
    if condition == 'low':
        amount = baseline2sequence[0] #just pick first, all the same
        sequence = baseline2sequence
        bsl_source_file = getBSLTaskSource(amount)
    elif condition == 'high':
        amount = baseline5sequence[0]
        sequence = baseline5sequence
        bsl_source_file = getBSLTaskSource(amount)
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

    ctlist = bslCTs[0:sequence_length]

    #debug purposes
    for ct in ctlist:
        ctlistIDs.append(ct.pk)

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

def setCTaskSources():
    ''' Makes a list of CTask source files with index = amount.'''
    global ctasksources
    all_sources = exp.external_source_data_set.filter(filetype = 'ctask')
    length = len(all_sources)
    ctasksources = [None]*len(all_sources)
    for i in all_sources:
        #amount begins with 2!!!
        index = i.external_choice_task_set.all()[0].amount -2
        ctasksources[index] = i
    # Same for baseline source files
    global bsltasksources
    all_sources = exp.external_source_data_set.filter(filetype = 'bltsk')
    bsltasksources = []
    for i in all_sources:
        bsltasksources.append(i)

def getCTaskSource(get_amount):
    return ctasksources[get_amount -2]

def getBSLTaskSource(get_amount):
    for bsl in bsltasksources:
        first_element = bsl.external_baseline_choice_task_set.all()[0]
        if first_element.amount == get_amount:
            return bsl
    else:
        raise Exception("We lack a BSL Source file.")


def getFreeCT(get_amount):
    amount_source = getCTaskSource(get_amount)
    try:
        assign_this_ct = amount_source.external_choice_task_set.order_by("used", "pk")[0]
        assign_this_ct.used = True
        assign_this_ct.save()
        # ordered = current_scale.external_order_scale_set.order_by("pk")
        # assign_this_scale = ordered.filter(linked_pcpt=None)[0]
    except:
        raise Exception('We ran out of '+amount+' choice tasks! Quick! We need more!')
    #write USED before return
    return assign_this_ct

# def getFreeCT(amount):
#     # ctasksources = exp.external_source_data_set.filter(filetype = 'ctask')
#     all_sources = ctasksources
#     cts_amount_source = None
#     for i in all_sources:
#         if i.external_choice_task_set.all()[0].amount == amount:
#             cts_amount_source = i
#     #the opposite of "used" is "-used" ! "+used" is invalid in bools.
#     cts_amount = cts_amount_source.external_choice_task_set.order_by("pk","used")[:2]
#     freeCT = None
#     for ct in cts_amount:
#         if ct.linked_pcpt == None:
#             freeCT = ct
#             break
#     if freeCT != None:
#         return freeCT
#     else:
#         raise Exception('- NO FREE CHOICE TASK, AMOUNT='+str(amount) +' ! -')
#         return 0
#

def createTasklist(condition):
    global ctlist
    global ctlistIDs
    cts = []
    #a set consists of 8(ctsetsize) tasks
    ctset = (ct_size / ctsetsize)
    if condition == 'increasing':
        sequence = increasingsequence
    elif condition == 'decreasing':
        sequence = decreasingsequence
    # amount_list = range(2,9,1)
    for s in range(0,ctset,1):
        # for a in amount_list:
        for a in sequence:
            cts.append(getFreeCT(a))
    #return:
    ctlist = cts
    #debug purposes
    for ct in ctlist:
        ctlistIDs.append(ct.pk)

def orderTasklist(rule):
    #operator order by key
    global ctlist
    the_list = ctlist
    tempList = []
    orderedList = []
    # amount_list = [2:8]
    if rule == 'increasing':
         law_order_temp = sorted(ctlist, key=operator.attrgetter('amount'))
         law_order = sorted(law_order_temp, key=operator.attrgetter('pk'))
         ctlist = law_order
         # pdb.set_trace()
    if rule == 'decreasing':
         law_order_temp = sorted(ctlist, key=operator.attrgetter('pk'))
         law_order = sorted(law_order_temp, key=operator.attrgetter('amount'), reverse=True)
         ctlist = law_order
         # pdb.set_trace()

def setChoiceTasks():
    global taskcounter
    global attributes
    taskcounter = 0
    attributes = exp.attribute_set.all()
    # pdb.set_trace()
    if group == 'baselinelow':
        createBaselineTasklist('low')
    if group == 'baselinehigh':
        createBaselineTasklist('high')
    if group == 'increasing':
        createTasklist('increasing')
        orderTasklist('increasing')
    if group == 'decreasing':
        createTasklist('decreasing')
        orderTasklist('decreasing')

def getAttributeLabelDict():
    #rc11 is always empty
    attribute_keys = ['rc21', 'rc31', 'rc41', 'rc51', 'rc61', 'rc71', 'rc81']
    attribute_values = [None]*len(attributes)
    temp = {}
    for a in attributes:
        attribute_values[a.position -1] = a.name
    for i in range (0, len(attribute_values),1):
        temp[attribute_keys[i]] = attribute_values[i]
    return temp

def checkNextTask(curr_page):
    if curr_page+1 < len(ctlist):
        return True
    else:
        return False

def checkNextConjoint(curr_conjoint):
    if curr_conjoint+1 < len(conjoint):
        return True
    else:
        return False

def getTask(task_nr):
    #maps a choice task to template: table.html
    #cells of attributes: can wait...
    attr = ctlist
    templ = {}
    task = ctlist[task_nr]
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
    if group in ('increasing','decreasing'):
        altModel = [task.a1, task.a2, task.a3, task.a4, task.a5, task.a6,task.a7, task.a8]
    elif group in ('baselinelow','baselinehigh'):
        altModel = [task.a1, task.a2, task.a3, task.a4, task.a5]
    for i in range(0, task.amount, 1):
        templ.update(mapCT(alts[i], altModel[i], i))
        #taskbysequenceviewn_amountofalternatives_choosenalternative_taskuniquepk
        templ[buybuttons[i]] = str(task_nr) + '_' + str(task.amount) + '_' + str(i+1) + '_' + str(task.pk)
    templ.update(getAttributeLabelDict())
    #finalize:
    return templ

def mapCT(dictKeys, rawvalues, nameindex):
    #prepare raw values
    optionSTR = ast.literal_eval(rawvalues)
    option = [int(x) for x in optionSTR]
    temp = {}
    #Option Header in table
    temp[dictKeys[0]] = 'Option '+ mapNameindex(nameindex)
    #uses +1 offset for header of alternative: 'a1'
    for j in range(1, len(option) +1, 1):
        temp[dictKeys[j]] = mapAttrLevel(option[j-1]-1, j)
    return temp

def mapNameindex(nameindex):
    return namelist[nameindex]

def mapAttrLevel(lvlvalue, attrposition):
    a = attributes.get(position = attrposition)
    output = a.level_set.get(value = lvlvalue).name
    return output

def initExp(exp_id):
    global exp
    global scales
    global group_all
    exp = Experiment.objects.get(pk = exp_id)
    setCTaskSources()
    scales = exp.external_source_data_set.filter(filetype = 'scale')
    jsonDec = json.decoder.JSONDecoder()
    group_all = jsonDec.decode(exp.grouping.group_nr)
    # raise Exception(model_to_dict(exp.grouping))


def initPcpt(ext_ct_size, ext_sessionid, ext_csrftoken, condition):
    '''Initiates a participant stub (pub).'''
    global scale_sequence
    # global pcpt_id
    global group
    global ct_size
    # global pub
    global scale_order_ids
    global id_hole_used
    ct_size = ext_ct_size
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

    group = getGroup(pcpt_id)
    ########################################################################
    #move to legacy?!
    # if (ext_pcpt_id == None): #should better be not used, too much confusion
        # has to be increased after pcpt.save() !!!
        # pcpt_id = exp.grouping.counter
    # else:
    #     try:
    #         valid_id = int(ext_pcpt_id)
    #         pcpt_id = valid_id
    #     except:
    #         raise Exception('The entered ID '+ str(ext_pcpt_id)+ ' is invalid!')
    #not yet implemented grouping:
    #group_all[pcpt_id]
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
    for scale in scale_names:
        scale_sequence[scale] = assignScaleOrder(scale)

    # debug purposes:
    for name, scale_object in scale_sequence.iteritems():
        scale_order_ids.append(scale_object.pk)

    # return infoObject(exp.grouping.counter, group, scale_sequence)
    #here's the cheese
    setChoiceTasks()

    #Save all to pub. Needed to mark files as "used"
    pub = Pub()
    pub.experiment = exp
    pub.ct_size = ct_size
    pub.hard_id = pcpt_id
    pub.sessionid = ext_sessionid
    pub.csrftoken = ext_csrftoken
    # pub.hard_id = exp.grouping.counter
    if condition == '':
        pub.def_group = getGroupDigit(group)
    else:
        pub.def_group = getGroupDigit(getGroup(pcpt_id))
        pub.override_group = getGroupDigit(group)

    #tag: write database
    pub.save()

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

    pubDict[pcpt_id] = pub
    return pcpt_id

def get_scale_context(scale_name_string):
    question_title = scale_questions.question_titles[scale_name_string]
    scale_name = scale_name_string
    scale_id = '' #css id design for the form! will STAY EMPTY!!!
    # print scale_sequence
    order_id = scale_sequence[scale_name_string].pk
    # pdb.set_trace()
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
    context = {'question_title': question_title,'scale_name':scale_name, 'scale_id':scale_id,'questions':questions , 'restoreCheck':restoreCheck}
    return context
