from django.conf.urls import patterns, include, url
##from djVacs.views import index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djVacs.views.home', name='home'),
    # url(r'^djVacs/', include('djVacs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eye/', include('eyevacs.urls')),
    #url(r'^polls/', include('polls.urls')),
)

urlpatterns += patterns('',
    url(r'^$', 'djVacs.views.index'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

'''
#same as:
urlpatterns += patterns('djVacs.views',
    url(r'^$', 'index'),
)
'''
