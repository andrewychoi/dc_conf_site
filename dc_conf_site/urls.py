from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dc_conf_site.views.home', name='home'),
    # url(r'^dc_conf_site/', include('dc_conf_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'register.views.index'),
    url(r'^index/$', 'register.views.index'),
    url(r'^attendants/$', 'register.views.attendants'),
    url(r'^organizers/$', 'register.views.organizers'),
    url(r'^program/$', 'register.views.program'),
    url(r'^register/$', 'register.views.register'),
    url(r'^report/$', 'register.views.report'),
    url(r'^venue/$', 'register.views.venue'),
)

urlpatterns += staticfiles_urlpatterns()