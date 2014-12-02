from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ContributorsList.as_view(), name='contributors-list'),
    url(r'^contributor/(?P<pk>\d+)/$', views.ContributorDetail.as_view(), name='contributor-detail'),
)
