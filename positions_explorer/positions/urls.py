from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^axis/?$', views.AxisDetail.as_view(), name='random-axis'),
    url(r'^axis/(?P<pk>\d+)/$', views.AxisDetail.as_view(), name='axis-detail'),
    url(r'^axis/results/(?P<pk>\d+)/$', views.AxisResults.as_view(), name='axis-detail'),
)
