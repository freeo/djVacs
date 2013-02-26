from eyevacs.models import Scale, Scale_Question, Experiment, Participant, External_Order_Scale
from scripts import scale_questions
import json
import re
import pdb

exp = None
scales = None
pcpt_id = None
group = None
groupName = {'1':'increasing','2':'decreasing','3':'baseline'}
scale_order_ids = {}
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']
session = {}
max_task_size = 21

def infoObject(*args):
    output = ''
    if len(args) > 0:
        for arg in args:
            try:
               output += int(arg) + '\n'
            except:
               output += str(arg) + '\n'
    return outpu


def getScale(scale_name_string):
    '''gets an External Source Data scale object.'''
    try:
        #pdb.set_trace()
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
    ctasklist = [None]*max_task_size
    for i in range(0,len(bsl_tasks),1):
        ctlist_index = bsl_tasks[i].task-1
        ctasklist[ctlist_index] = bsl_tasks[i]
    return ctasklist

def createTasklist():
    sources = exp.external_source_data_set.filter(filetype = 'ctask')
    #for source in sources:



def getChoiceTasks():
    global ctasklist
    ctasklist = []
    if groupName[str(group)] == 'baseline':
        ctasklist = createBaselineTasklist()
    #increasing and decreasing
    else:
        ctasklist = ['none in tasklist, inc dec group']



def initPcpt(exp_id):
    global exp
    global scales
    global scale_order_ids
    global pcpt_id
    global group
    exp = Experiment.objects.get(pk = exp_id)
    scales = exp.external_source_data_set.filter(filetype = 'scale')
    jsonDec = json.decoder.JSONDecoder()
    group_all = jsonDec.decode(exp.grouping.group_nr)
    pcpt_id = exp.grouping.counter # has to be increased after pcpt.save() !!!
    group = 3 #group_all[pcpt_id]
    for scale in scale_names:
        scale_order_ids[scale] = assignScaleOrder(scale)
    # return infoObject(exp.grouping.counter, group, scale_order_ids)
    getChoiceTasks()



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
        qid = question_order[i]
        q = {'text':qtext,'id':qid}
        questions.append(q)
    lb_button_continue = 'Continue'
    context = {'question_title': question_title,'scale_name':scale_name, 'scale_id':scale_id,'questions':questions ,'lb_button_continue':lb_button_continue, 'restoreCheck':restoreCheck}
    return context
