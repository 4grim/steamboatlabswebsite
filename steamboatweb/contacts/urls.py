from django.conf.urls import patterns, url
from contacts import views

urlpatterns = patterns('',
	url(r'^contact_index/$', views.contact_index, name='contact_index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^contact/thanks/(?P<message_id>\d+)/$', views.contact_submitted, name='contact_submitted'),
	)