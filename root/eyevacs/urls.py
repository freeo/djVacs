from django.conf.urls import patterns, url #include

#/eye/expID/pcptID/
pcptID = r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/'+'%s'+r'$'

urlpatterns = patterns('eyevacs.views',
    url(r'^$', 'eye'),
    url(r'^lang/$', 'set_language'),
    url(r'^exp(?P<exp_id>\d+)/$','exp'),
    url(r'^exp(?P<exp_id>\d+)/outputcsv/$','outputCSV'),
    url(r'^exp(?P<exp_id>\d+)/removepubs/$','removepubs'),
    url(r'^exp(?P<exp_id>\d+)/resetidholes/$','resetIDholes'),
    url(r'^exp(?P<exp_id>\d+)/preparePcpt/$','preparePcpt'),
    url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt_id>\d+)/$','pcptInfo'),
    # url(r'^exp(?P<exp_id>\d+)/welcome/$','welcome'),                #/eye/expID/
    url( pcptID % r'debug/','singlePageDebug'),
    url( pcptID % r'welcome/','welcome'),
    # url( pcptID % r'welcome/','welcome'), #/eye/expID/pcptID/welcome
    url( pcptID % r'rnd_max/','rnd_max'),
    url( pcptID % r'rnd_regret/','rnd_regret'),
    url( pcptID % r'pl_experience/','pl_experience'),
    url( pcptID % r'rnd_involvement/','rnd_involvement'),
    url( pcptID % r'explanation/0_overview/','explanation_overview'),
    url( pcptID % r'explanation/1_food/','explanation_food'),
    url( pcptID % r'explanation/2_recommend/','explanation_recommend'),
    url( pcptID % r'explanation/3_distance/','explanation_distance'),
    url( pcptID % r'explanation/4_seaview/','explanation_seaview'),
    url( pcptID % r'explanation/5_price/','explanation_price'),
    url( pcptID % r'explanation/6_room/','explanation_room'),
    url( pcptID % r'explanation/7_favattributes/','explanation_favattributes'),
    url( pcptID % r'explanation/8_ctseqintro/','explanation_ctseqintro'),
    url( pcptID % r'ct(?P<ct_page>\d+)/','decisionsequence'),
    url( pcptID % r'ct(?P<ct_page>\d+)/loading/','loadingsequence'),
    url( pcptID % r'conjoint/(?P<conjoint_id>\d+)/','conjoint'),
    url( pcptID % r'conjoint/loading/','loadingconjoint'),
    url( pcptID % r'transit/overview/','transit'),
    url( pcptID % r'transit/hotel1/','hotel1'),
    url( pcptID % r'transit/hotel2/','hotel2'),
    url( pcptID % r'transit/hotel3/','hotel3'),
    url( pcptID % r'transit/hotel4/','hotel4'),
    url( pcptID % r'transit/hotel5/','hotel5'),
    url( pcptID % r'transit/hotel6/','hotel6'),
    url( pcptID % r'transit/select/','transit_select'),
    url( pcptID % r'rnd_searchgoals/','rnd_searchgoals'),
    url( pcptID % r'rnd_happiness/','rnd_happiness'),
    url( pcptID % r'pl_demographics/','pl_demographics'),
    url( pcptID % r'finalPage/','finalPage'),
    url(r'^exp4/pcpt6/debugsaving/$','debugsaving'),

    url(r'^temp/$', 'temp'),

    #url(r'^exp(?P<exp_name>[a-z]{1,10})/$','experiment_name'),
    #url(r'^exp-(?P<exp_id>\d+)/$','experiment_id'),
)
