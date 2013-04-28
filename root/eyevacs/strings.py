# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy

########################################################################
########## SCALE QUESTIONS #############################################
########################################################################

scales = {}
rnd_files = []
scale_names = ['rnd_max', 'rnd_regret', 'rnd_involvement', 'rnd_searchgoals', 'rnd_happiness']
rnd_max_questions = [ugettext_lazy(u'When I am in the car listening to the radio, I often check other stations to see if something better is playing, even if I am relatively satisfied with what I’m listening to.'),ugettext_lazy(u'No matter how satisfied I am with my job, it’s only right for me to be on the lookout for better opportunities.'),ugettext_lazy(u'I often find it difficult to shop for a gift for a friend.'),ugettext_lazy(u'Renting videos is really difficult. I’m always struggling to pick the best one.'),ugettext_lazy(u'No matter what I do, I have the highest standards for myself.'),ugettext_lazy(u'I never settle for second best.')]
rnd_regret_questions = [ugettext_lazy(u'Whenever I make a choice, I’m curious about what would have happened if I had chosen differently.'), ugettext_lazy(u'Whenever I make a choice, I try to get information about how the other alternatives turned out.'), ugettext_lazy(u'If I make a choice and it turns out well, I still feel like something of a failure if I find out that another choice would have turned out better.'), ugettext_lazy(u'When I think about how I’m doing in life, I often assess opportunities I have passed up.'), ugettext_lazy(u'Once I make a decision, I don’t look back.')]
rnd_involvement_questions = [ugettext_lazy(u'Overall, how familiar are you with booking vacation packages?'), ugettext_lazy(u'The decision which vacation package to book is a'), ugettext_lazy(u'The decision which vacation package to book'), ugettext_lazy(u'When booking a vacation package there is') ]
rnd_searchgoals_questions = [ugettext_lazy(u'Even if I found a vacation package that I was relatively satisfied with, I still looked to the other available vacation packages before deciding.'), ugettext_lazy(u'I tried to find the best vacation package.'), ugettext_lazy(u'I had in mind some ideal vacation package(s), and I tried to look for vacation packages similar to my ideal package(s).'), ugettext_lazy(u'I made my decision as soon as I found a vacation package that was good enough. ')]
rnd_happiness_questions = [ugettext_lazy(u'In general, I consider myself:'), ugettext_lazy(u'Compared to most of my peers, I consider myself:'), ugettext_lazy(u'Some people are generally very happy. They enjoy life regardless of what is going on, getting the most out of everything. To what extent does this characterization describe you?'), ugettext_lazy(u'Some people are generally very happy. They enjoy life regardless of what is going on, getting the most out of everything. To what extent does this characterization describe you?')]

########################################################################

rnd_max_title = ugettext_lazy(u'Welcome to the study on vacation packages!<br/><br/>We’d like to start with some general statements about how you behave in daily situations. <br/>Please indicate your degree of agreement with the following statements (-3 = I do not agree with the statement at all, +3 = I agree with the statement very much)')

rnd_regret_title = ugettext_lazy(u'The following statements are related to choices in daily situations. <br/>Please indicate your degree of agreement with the following statements (-3 = I do not agree with the statement at all, +3 = I agree with the statement very much)')

rnd_involvement_title = ugettext_lazy(u'What would you say:')

rnd_searchgoals_title = ugettext_lazy(u'We’d like to learn how you proceeded when making your <b>last</b> choice:')

rnd_happiness_title = ugettext_lazy(u'For each of the following statements and/or questions, please mark the point on the scale that you feel is most appropriate in describing you.')

########################################################################

question_titles = {'rnd_max':rnd_max_title,'rnd_regret':rnd_regret_title, 'rnd_involvement':rnd_involvement_title,'rnd_searchgoals':rnd_searchgoals_title, 'rnd_happiness':rnd_happiness_title}
########################################################################
#
rnd_max_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_regret_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_involvement_caption = [{'left':ugettext_lazy('very unfamiliar'),'right':ugettext_lazy('very familiar')},{'left':ugettext_lazy('very unimportant decision'),'right':ugettext_lazy('very important decision')},{'left':ugettext_lazy('requires little thought'),'right':ugettext_lazy('requires a lot of thought')},{'left':ugettext_lazy('little to lose if you choose the wrong package'),'right':ugettext_lazy('a lot to lose if you choose the wrong package')}]
rnd_searchgoals_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]
rnd_happiness_caption = [{'left':ugettext_lazy('not a very happy person'),'right':ugettext_lazy('a very happy person')},{'left':ugettext_lazy('less happy'),'right':ugettext_lazy('more happy')},{'left':ugettext_lazy('not at all'),'right':ugettext_lazy('great deal')},{'left':ugettext_lazy('not at all'),'right':ugettext_lazy('a great deal')}]

question_captions = {'rnd_max':rnd_max_caption,'rnd_regret':rnd_regret_caption, 'rnd_involvement':rnd_involvement_caption,'rnd_searchgoals':rnd_searchgoals_caption, 'rnd_happiness':rnd_happiness_caption}

########################################################################

questions = {'rnd_max':rnd_max_questions,'rnd_regret':rnd_regret_questions, 'rnd_involvement':rnd_involvement_questions,'rnd_searchgoals':rnd_searchgoals_questions, 'rnd_happiness':rnd_happiness_questions}

########################################################################
########### PL_DIFFICULTY PAGES ########################################
########################################################################


difficulty_last_title= ugettext_lazy(u'Regarding <b>only</b> your last choice:')

pl_difficulty_questions = [
    ugettext_lazy(u'How difficult was it for you to choose the vacation package you wanted when last making a choice?'),
    ugettext_lazy(u'How frustrated did you feel when making the choice?'),
    ugettext_lazy(u'How hesitant did you feel when making the choice?'),
    ugettext_lazy(u'How similar did you find the options were to one another?')]

pl_difficulty_questions_idnames = [
    'choice_difficulty',
    'frustration',
    'hesitation',
    'similarity',
    ]

pl_difficulty_caption = [{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''},{'left':'','right':''}]

difficulty_titles = {
        'difficulty_last':difficulty_last_title
    }

########################################################################
########## HOLDOUT TITLES ##############################################
########################################################################

holdout_title_1=ugettext_lazy("Let's come back to two more choices between hotels. <br/> If these hotels were your only options, which hotel would you buy for you and your friend with the money you got from your relative?")

holdout_title_2=ugettext_lazy("If these hotels were your only options, which hotel would you buy for you and your friend with the money you got from your relative?")
