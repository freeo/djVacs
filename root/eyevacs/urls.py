from django.conf.urls import patterns, url #include

#/eye/expID/pcptID/
pcptID = r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/'+'%s'+r'$'

urlpatterns = patterns('eyevacs.views',
    url(r'^$', 'eye'),                                  #/eye/
    url(r'^lang/$', 'set_language'),                    #/eye/lang/
    url(r'^exp(?P<exp_id>\d+)/$','exp'),                #/eye/expID/
    #url(r'^exp(?P<exp_id>\d+)/collect/$','collect'),     #/eye/expID/collect/
    url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/$','pcptInfo'),
    url( pcptID % r'welcome/','welcome'),              #/eye/expID/pcptID/welcome
    url( pcptID % r'rnd_max/','rnd_max'),              #/eye/expID/pcptID/rnd_max
    url( pcptID % r'rnd_regret/','rnd_regret'),           #/eye/expID/pcptID/rnd_regret
    url( pcptID % r'pl_experience/','pl_experience'),           #/eye/expID/pcptID/rnd_regret
    url( pcptID % r'explanation/','explanation'),           #/eye/expID/pcptID/explanation
    #CHOICE TASKS
    url( pcptID % r'ct(?P<ct_page>\d+)/','decisionsequence'),           #/eye/expID/pcptID/rnd_regret
    url( pcptID % r'rnd_searchgoals/','rnd_searchgoals'),           #/eye/expID/pcptID/rnd_regret
    url( pcptID % r'rnd_happiness/','rnd_happiness'),           #/eye/expID/pcptID/rnd_regret
    url( pcptID % r'pl_demographics/','pl_demographics'),           #/eye/expID/pcptID/srnd_regret
    #/eye/expID/pcptID/
    #url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt>\d+)/$','participant'),
                                                        #/eye/expID/pcptID/pgPAGENO/
    #url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt>\d+)/pg(?P<page>\d+)/$','page'),

    url(r'^temp/$', 'temp'),

    #url(r'^exp(?P<exp_name>[a-z]{1,10})/$','experiment_name'),
    #url(r'^exp-(?P<exp_id>\d+)/$','experiment_id'),
)


