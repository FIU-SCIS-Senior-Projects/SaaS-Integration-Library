from django.conf.urls import patterns, url
from SIL import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^datasource/$', views.datasource, name='datasource'),
                       url(r'^datasource/confirmation/(?P<api_name>\w{0,50})/$', views.confirmation, name ='confirmation'),
                       url(r'^api/$', views.datasets, name='datasets'),
                       url(r'^api/(?P<api_name>\w+)/$', views.api, name='api'),
                       url(r'^api/(?P<api_name>\w+)/(?P<action_name>\w+)$', views.apicall, name='apicall'))

