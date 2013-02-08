from django.conf.urls import patterns, url #include

urlpatterns = patterns('eyevacs.views',
    url(r'^$', 'eye'),                                  #/eye/
    url(r'^lang/$', 'set_language'),                    #/eye/lang/
    url(r'^exp(?P<exp_id>\d+)/$','experiment_id'),      #/eye/expID/
                                                        #/eye/expID/pcptinit/
    url(r'^exp(?P<exp_id>\d+)/pcptinit/$','initParticipant'),
                                                        #/eye/expID/pcptID/
    url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt>\d+)/$','participant'),
                                                        #/eye/expID/pcptID/pgPAGENO/
    url(r'^exp(?P<exp_id>\d+)/pcpt(?P<pcpt>\d+)/pg(?P<page>\d+)/$','page'),

    url(r'^temp/$', 'temp'),

    #url(r'^exp(?P<exp_name>[a-z]{1,10})/$','experiment_name'),
    #url(r'^exp-(?P<exp_id>\d+)/$','experiment_id'),
)


