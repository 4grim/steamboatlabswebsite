from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^projects/$', views.project_index, name='project_index'),
	url(r'^projects/(?P<project_id>\d+)/$', views.project_page, name='project_page'),
	)