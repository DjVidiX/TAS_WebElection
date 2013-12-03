from django.conf.urls import patterns, include, url
from TAS_WebElection.views import home, candidates, contact


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', home),
                       url(r'^kandydaci', candidates, name='candidates'),
                       url(r'^kontakt', contact, name='contact'),
                       # url(r'^TAS_WebElection/', include('TAS_WebElection.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^administrator/', include(admin.site.urls)),
)
