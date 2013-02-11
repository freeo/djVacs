from eyevacs.models import Scale, Scale_Question, Experiment, Participant, External_Order_Scale
from scripts import scale_questions
import json
import pdb


exp = None
scales = None
pcpt_id = None
scale_order_ids = {}
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']


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

def assignScaleOrder(scale_name_string):
    current_scale = getScale(scale_name_string)
    current_orderings = current_scale.external_order_scale_set.all()
    upper_range = len(current_orderings)
    for i in range(0,upper_range,1):
        if current_orderings[i].linked_pcpt == None:
            return current_orderings[i].pk
            break

def initPcpt(exp_id):
    global exp
    global scales
    global scale_order_ids
    exp = Experiment.objects.get(pk = exp_id)
    scales = exp.external_source_data_set.filter(filetype = 'scale')
    jsonDec = json.decoder.JSONDecoder()
    group_all = jsonDec.decode(exp.grouping.group_nr)
    pcpt_id = exp.grouping.counter # has to be increased after pcpt.save() !!!
    group = group_all[pcpt_id]
    #pdb.set_trace()
    for scale in scale_names:
        scale_order_ids[scale] = assignScaleOrder(scale)
        #pdb.set_trace()
    # return infoObject(exp.grouping.counter, group, scale_order_ids)

def get_scale_context(scale_name_string):
    #  abc = getScale(scale_name_string)
    question_title = scale_questions.question_titles[scale_name_string]
    next_page = './temp/'
    scale_name = scale_name_string
    scale_id = '' #css id design for the form! will STAY EMPTY!!!
    print scale_order_ids
    #pdb.set_trace()
    order_id = scale_order_ids[scale_name_string]
    question_order = map(int, External_Order_Scale.objects.get(pk=order_id).scale_rnd_order_ext.split(','))
    questions = []
    for i in range(0, len(question_order),1):
        qtext = scale_questions.questions[scale_name_string][question_order[i]-1]
        qid = question_order[i]
        q = {'text':qtext,'id':qid}
        questions.append(q)
    name_scale_continue_button = scale_name_string + '_button'
    bt_continue_id = ''
    lb_button_continue = 'Continue'
    context = {'question_title': question_title,'next_page':next_page,'scale_name':scale_name, 'scale_id':scale_id,'questions':questions,'name_scale_continue_button':name_scale_continue_button ,'bt_continue_id':bt_continue_id ,'lb_button_continue':lb_button_continue}
    return context
