from django.conf.urls import url, patterns, include

from readthedocs.gold import views


urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='gold_register'),
                       url(r'^edit/$', views.edit, name='gold_edit'),
                       url(r'^cancel/$', views.cancel, name='gold_cancel'),
                       url(r'^thanks/$', views.thanks, name='gold_thanks'),
                       )
