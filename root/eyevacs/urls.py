from django.conf.urls import patterns, url #include

#/eye/expID/pcptID/
pcptID = r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/'+'%s'+r'$'

urlpatterns = patterns('eyevacs.views',
    url(r'^$', 'eye'),
    url(r'^lang/$', 'set_language'),
    url(r'^exp(?P<exp_id>\d+)/$','exp'),
    url(r'^exp(?P<exp_id>\d+)/preparePcpt/$','preparePcpt'),
    url(r'^exp(?P<exp_id>\d+)/debug/$','singlePageDebug'),
    url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/$','pcptInfo'),
    url(r'^exp(?P<exp_id>\d+)/welcome/$','welcome'),                #/eye/expID/
    # url( pcptID % r'welcome/','welcome'),              #/eye/expID/pcptID/welcome
    url( pcptID % r'rnd_max/','rnd_max'),
    url( pcptID % r'rnd_regret/','rnd_regret'),
    url( pcptID % r'pl_experience/','pl_experience'),
    url( pcptID % r'explanation/','explanation'),
    url( pcptID % r'ct(?P<ct_page>\d+)/','decisionsequence'),
    url( pcptID % r'conjoint/','conjoint'),
    url( pcptID % r'transit/','transit'),
    url( pcptID % r'rnd_searchgoals/','rnd_searchgoals'),
    url( pcptID % r'rnd_happiness/','rnd_happiness'),
    url( pcptID % r'pl_demographics/','pl_demographics'),
    url( pcptID % r'finalPage/','finalPage'),

    url(r'^temp/$', 'temp'),

    #url(r'^exp(?P<exp_name>[a-z]{1,10})/$','experiment_name'),
    #url(r'^exp-(?P<exp_id>\d+)/$','experiment_id'),
)


