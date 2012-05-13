from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from know_crawler_site.scheduler import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'know_crawler_site.views.home', name='home'),
    # url(r'^know_crawler_site/', include('know_crawler_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^scheduler/$', views.sheduler),
)
