from django.conf.urls import patterns, url
from uploads import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^upload_page/$', views.upload_page, name='upload_page'),
    url(r'^upload_action/$', views.upload_action, name='upload_action'),
    url(r'^classfy/$', views.classfy, name='classfy'),
    url(r'^repository/$', views.repository, name='repository'),
    url(r'^cats/$', views.cats, name='cats'),
    url(r'^dogs/$', views.dogs, name='dogs'),
    url(r'^empty_repository/$', views.empty_repository, name='empty_repository'),
)
