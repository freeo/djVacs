from eyevacs.models import Scale, Scale_Question, Experiment, Participant
import eyevacs.maximization

exp = None
pcpt_id = None
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']

def getScale(scale_name_string):


def assignScaleOrder(scale_name_string):
    ext_source_data_scale = External_Source_Data.objects.filter(header.lower() = scale_name_string.lower())
    selected_scale = exp.scale_set.filter(name.lower() = scale_name_string)
    upper_range = len(ext_source_data_scale.external_order_scale_set)
    entire_set = ext_source_data_scale.external_order_scale_set
    for i in range(0,upper_range,1):
        if entire_set[i].linked_pcpt == None:
            #get its hard id?

def initPcpt(exp_id):
    global exp
    exp = Experiment.objects.get(pk = exp_id)
    group = #inc dec bsl
    scale_orders = {}
    for scale in scale_names:
        scale_orders[scale] = assignMaxScaleOrder(scale)


def get_scale_context(pcpt_id, scale_name_string):
    abc = getScale(scale_name_string)
    question_title =
    next_page =
    scale_name =
    scale_id =
    qtext =
    qid =
    questions = {'text':qtext,'id':qid}
    name_scale_continue_button =
    bt_continue_id =
    lb_button_continue =
    context = {'question_title': question_title,'next_page':next_page,'scale_name':scale_name, 'scale_id':scale_id,'questions ':questions  ,'name_scale_continue_button':name_scale_continue_button ,'bt_continue_id':bt_continue_id ,'lb_button_continue':lb_button_continue}
