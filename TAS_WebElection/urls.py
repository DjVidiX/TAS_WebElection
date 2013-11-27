from django.conf.urls import patterns, include, url
from TAS_WebElection.views import home, candidates, vote, index


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', home),
                       url(r'^kandydaci', candidates, name='candidates'),
                       url(r'^glosuj', vote, name='vote'),
                       url(r'^lol', index, name='lool'),
                       url(r'^lol#admin', candidates, name='candidates'),
                       # url(r'^TAS_WebElection/', include('TAS_WebElection.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
