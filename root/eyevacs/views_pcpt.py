from eyevacs.models import Scale, Scale_Question, Experiment, Participant, External_Order_Scale, Attribute, Level
from scripts import scale_questions
import json
import re
import ast
import pdb

ctsetsize = 7

exp = None
scales = None
pcpt_id = None
group = None
ct_size = None #choice task size for this.pcpt.id, can vary within experiment
ctasksources = None
ctlist = []
attributes = None
taskcounter = None
ct_bsl_list = []
validatedCTs = {}
groupName = {'1':'increasing','2':'decreasing','3':'baselinehigh','4':'baselinelow'}
scale_order_ids = {}
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']
# session = {}
namelist = ['A','B','C','D','E','F','G','H']
max_task_size = 21
conjoint1={'id':'1','food':'good','recommending':'90%','distance':'1 km','view':'no sea view','price':'$699','room':'standard'}
conjoint2={'id':'2','food':'good','recommending':'90%','distance':'3 km','view':'full sea view','price':'$699','room':'deluxe'}
conjoint3={'id':'3','food':'excellent','recommending':'90%','distance':'1 km','view':'no sea vie','price':'$899','room':'deluxe'}
conjoint4={'id':'4','food':'good','recommending':'50%','distance':'1 km','view':'full sea view','price':'$899','room':'deluxe'}
conjoint5={'id':'5','food':'excellent','recommending':'50%','distance':'1 km','view':'full sea view','price':'$699','room':'standard'}
conjoint6={'id':'6','food':'excellent','recommending':'90%','distance':'3 km','view':'full sea view','price':'$899','room':'standard'}
conjoint7={'id':'7','food':'good','recommending':'50%','distance':'3 km','view':'no sea view','price':'$899','room':'standard'}
conjoint8={'id':'8','food':'excellent','recommending':'50%','distance':'3 km','view':'no sea view','price':'$699','room':'deluxe'}
conjoint = [conjoint1,conjoint2,conjoint3,conjoint4,conjoint5,conjoint6,conjoint7,conjoint8]

def getConjoint(index):
    return conjoint[index]

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
    current_orderings = current_scale.external_order_scale_set.all()
    upper_range = len(current_orderings)
    for i in range(0,upper_range,1):
        if current_orderings[i].linked_pcpt == None:
            return current_orderings[i].pk
            break

def incrementTaskCounter():
    global taskcounter
    taskcounter += 1

def createBaselineTasklist():
    #get bsl by hard id, set linked pcpt of id x after save()
    bsl_id = None
    bsl_source_file = exp.external_source_data_set.filter(filetype = 'bltsk')
    #is unique, just use index 0
    bslCTs = bsl_source_file[0].external_baseline_choice_task_set.all()
    notFound = 1
    while notFound:
        i = 0
        if bslCTs[i].linked_pcpt == None:
            bsl_id = bslCTs[i].id_hard
            notFound = 0
            break
        else:
            if i < len(bslCTs):
                i += 1
            else:
                print 'no free baseline choice tasks left... must be a bug.'
                notFound = 0
                break
    bsl_tasks = bslCTs.filter(id_hard = bsl_id)
    #exp.External_Baseline_Choice_Task.objects.filter(id_hard = bsl_id)
    ct_bsl_list = [None]*max_task_size
    for i in range(0,len(bsl_tasks),1):
        ctlist_index = bsl_tasks[i].task-1
        ct_bsl_list[ctlist_index] = bsl_tasks[i]
    return ct_bsl_list

# def createTasklist():
#     ctasksources = exp.external_source_data_set.filter(filetype = 'ctask')
    #for source in sources:

def getFreeCT(amount):
    # ctasksources = exp.external_source_data_set.filter(filetype = 'ctask')
    all_sources = ctasksources
    cts_amount_source = None
    for i in all_sources:
        if i.external_choice_task_set.all()[0].amount == amount:
            cts_amount_source = i
    #the opposite of "used" is "-used" ! "+used" is invalid in bools.
    cts_amount = cts_amount_source.external_choice_task_set.order_by("pk","used")[:2]
    freeCT = None
    for ct in cts_amount:
        if ct.linked_pcpt == None:
            freeCT = ct
            break
    if freeCT != None:
        return freeCT
    else:
        raise Exception('- NO FREE CHOICE TASK, AMOUNT='+str(amount) +' ! -')
        return 0

def createTasklist():
    global ctlist
    cts = []
    #a set consists of 7(ctsetsize) tasks
    ctset = (ct_size / ctsetsize)
    amount_list = range(2,9,1)
    for s in range(0,ctset,1):
        for a in amount_list:
            cts.append(getFreeCT(a))
    ctlist = cts

def orderTasklist(rule):
    #operator order by key
    global ctlist
    tempList = []
    orderedList = []
    # amount_list = [2:8]
    if rule == 'increasing':
         # for s in range(0,ctset,1):
         #    for ct in range(0,ctsetsize,1):
         #        for a in amount_list:
         #            ctlist
         # for ct in ctlist:
         print 'b'

    if rule == 'decreasing':
         print 'b'

def setChoiceTasks():
    global ct_bsl_list
    global taskcounter
    global attributes
    taskcounter = 0
    attributes = exp.attribute_set.all()
    if groupName[str(group)] == 'baseline':
        ct_bsl_list = createBaselineTasklist()
    #increasing and decreasing
    if groupName[str(group)] == 'increasing':
        createTasklist()
        orderTasklist('increasing')
    if groupName[str(group)] == 'decreasing':
        createTasklist()
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
    altModel = [task.a1, task.a2, task.a3, task.a4, task.a5, task.a6,task.a7, task.a8]
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

    # global labels
    # for a in attributes:
    #     labels[a.name] = a.level_set.all()


def initPcpt(exp_id, ext_ct_size, ext_pcpt_id = None):
    global exp
    global scales
    global scale_order_ids
    global pcpt_id
    global group
    global ct_size
    global ctasksources
    exp = Experiment.objects.get(pk = exp_id)
    ctasksources = exp.external_source_data_set.filter(filetype = 'ctask')
    scales = exp.external_source_data_set.filter(filetype = 'scale')
    try:
        ct_size = int(ext_ct_size)
    except:
        raise Exception('Not a valid ct_size! Is a bug or a hack, cant be.')
    jsonDec = json.decoder.JSONDecoder()
    group_all = jsonDec.decode(exp.grouping.group_nr)
    if (ext_pcpt_id == None):
        # has to be increased after pcpt.save() !!!
        pcpt_id = exp.grouping.counter
    else:
        try:
            valid_id = int(ext_pcpt_id)
            pcpt_id = valid_id
        except:
            raise Exception('The entered ID '+ str(ext_pcpt_id)+ ' is invalid!')
    group = 1 #group_all[pcpt_id]
    for scale in scale_names:
        scale_order_ids[scale] = assignScaleOrder(scale)
    # return infoObject(exp.grouping.counter, group, scale_order_ids)
    setChoiceTasks()

def get_scale_context(scale_name_string):
    question_title = scale_questions.question_titles[scale_name_string]
    scale_name = scale_name_string
    scale_id = '' #css id design for the form! will STAY EMPTY!!!
    print scale_order_ids
    order_id = scale_order_ids[scale_name_string]
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
