# -*- coding: utf-8 -*-
from eyevacs.models import Experiment, Scale, Scale_Question, External_Source_Data
from django.utils.translation import ugettext

scales = {}
rnd_files = []
exp = None
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']
rnd_max_questions = [ugettext(u'When I am in the car listening to the radio, I often check other stations to see if something better is playing, even if I am relatively satisfied with what I’m listening to.'),ugettext(u'No matter how satisfied I am with my job, it’s only right for me to be on the lookout for better opportunities.'),ugettext(u'I often find it difficult to shop for a gift for a friend.'),ugettext(u'Renting videos is really difficult. I’m always struggling to pick the best one.'),ugettext(u'No matter what I do, I have the highest standards for myself.'),ugettext(u'I never settle for second best.')]
rnd_regret_questions = [ugettext(u'Whenever I make a choice, I’m curious about what would have happened if I had chosen differently.'), ugettext(u'Whenever I make a choice, I try to get information about how the other alternatives turned out.'), ugettext(u'If I make a choice and it turns out well, I still feel like something of a failure if I find out that another choice would have turned out better.'), ugettext(u'When I think about how I’m doing in life, I often assess opportunities I have passed up.'), ugettext(u'Once I make a decision, I don’t look back.')]
rnd_involvement_questions = [ugettext(u'Overall, how familiar are you with booking vacation packages?'), ugettext(u'The decision which vacation package to buy is a'), ugettext(u'The decision which vacation package to buy'), ugettext(u'When booking a vacation package there is') ]
rnd_searchgoals_questions = [ugettext(u'Even if I found a vacation package that I was relatively satisfied with, I still looked to the other available vacation packages before deciding.'), ugettext(u'I tried to find the best vacation package in each of the previous choice tasks.'), ugettext(u'I had in mind some ideal vacation package(s), and I tried to look for vacation packages similar to my ideal package(s).'), ugettext(u'I made my decision in each choice task as soon as I found a vacation package that was good enough. ')]
rnd_happiness_questions = [ugettext(u'In general, I consider myself:'), ugettext(u'Compared to most of my peers, I consider myself:'), ugettext(u'Some people are generally very happy. They enjoy life regardless of what is going on, getting the most out of everything. To what extent does this characterization describe you?'), ugettext(u'Some people are generally very happy. They enjoy life regardless of what is going on, getting the most out of everything. To what extent does this characterization describe you?')]

##XXX###################################################################

rnd_max_title = ugettext(u'We’d like to start with some general statements about how you behave in daily situations. \nPlease indicate your degree of agreement with the following statements (-3 = I do not agree with the statement at all, +3 = I agree with the statement very much)')

rnd_regret_title = ugettext(u'The following statements are related to choices in daily situations. \nPlease indicate your degree of agreement with the following statements (-3 = I do not agree with the statement at all, +3 = I agree with the statement very much)')

rnd_involvement_title = ugettext(u'What would you say:')

rnd_searchgoals_title = ugettext(u'Now let’s come back to the hotel choices you made for you and your friend with the money you got from your rich relative (the $2000). We’d like to learn how you proceeded when making these choices:\n\nPlease indicate your degree of agreement with the following statements (-3 = I do not agree with the statement at all, +3 = I agree with the statement very much)')

rnd_happiness_title = ugettext(u'For each of the following statements and/or questions, please mark the point on the scale that you feel is most appropriate in describing you.')

########################################################################

question_titles = {'rnd_max':rnd_max_title,'rnd_regret':rnd_regret_title, 'rnd_involvement':rnd_involvement_title,'rnd_searchgoals':rnd_searchgoals_title, 'rnd_happiness':rnd_happiness_title}
########################################################################
#
rnd_max_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_regret_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_involvement_caption = [{'left':ugettext('very unfamiliar'),'right':ugettext('very familiar')},{'left':ugettext('very unimportant decision'),'right':ugettext('very important decision')},{'left':ugettext('requires little thought'),'right':ugettext('requires a lot of thought')},{'left':ugettext('little to lose if you choose the wrong package'),'right':ugettext('a lot to lose if you choose the wrong package')}]
rnd_searchgoals_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_happiness_caption = [{'left':ugettext('not a very happy person'),'right':ugettext('a very happy person')},{'left':ugettext('less happy'),'right':ugettext('more happy')},{'left':ugettext('not at all'),'right':ugettext('great deal')},{'left':ugettext('not at all'),'right':ugettext('a great deal')}]

question_captions = {'rnd_max':rnd_max_caption,'rnd_regret':rnd_regret_caption, 'rnd_involvement':rnd_involvement_caption,'rnd_searchgoals':rnd_searchgoals_caption, 'rnd_happiness':rnd_happiness_caption}

########################################################################

questions = {'rnd_max':rnd_max_questions,'rnd_regret':rnd_regret_questions, 'rnd_involvement':rnd_involvement_questions,'rnd_searchgoals':rnd_searchgoals_questions, 'rnd_happiness':rnd_happiness_questions}

def load_rnd_files():
    global rnd_files
    #print exp
    rnd_files = exp.external_source_data_set.filter(filetype='scale')

# def __init__():
#     loadScales()

def get_rnd_file(name_string):
    #try:
    for rnd in rnd_files:
        #print rnd.header, name_string, rnd_files
        if rnd.header.lower() == name_string.lower():
            return rnd
    # except:
    #     print len(rnd_files)
    #     print '--- error, no rnd file of that name ---'
    #     raise Exception(rnd_files, rnd)

def import_scale(scale_name_string):
    rnd_file_exp = get_rnd_file(scale_name_string)
    # print exp
    # print scale_name_string
    # print rnd_file_exp
    scale = Scale(name = scale_name_string, experiment = exp, rnd_file = rnd_file_exp)
    for question in questions[scale_name_string]:
        scale_question = Scale_Question(linked_scale = scale, text = question, id_order = questions[scale_name_string].index(question)+1)
        scale_question.save()
    scale.save() #write to database
    scales[scale_name_string] = scale #write to scale dictionary

def getScale(dict_name_string):
    #get by name string, hard coded into the dictionary
    return scales[dict_name_string]
    #scale questions:
    #scale.scale_questions_set.all()

def getScaleNames():
    return scale_names

#__main__
def load_scale_questions(curr_exp):
    global exp
    exp = curr_exp
    load_rnd_files()
    for scale_name in scale_names:
        import_scale(scale_name)
    print '--- Scale questions have been installed/updated --- '


