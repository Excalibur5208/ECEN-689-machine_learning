from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^hello/$', views.hello, name='hello'),
	url(r'^current_datetime/$', views.current_datetime),
	url(r'^(?P<str0>[\w]+)/$', views.just_for_fun, name='just_for_fun'),
)