from django.conf.urls import url
from recruiter import views

app_name = 'recruiter'

urlpatterns=[
    url(r'^technologyverticals/$', views.technologyvertical_list),
    url(r'^technologyverticals/(?P<pk>[0-9]+)$', views.technologyvertical_detail),
    url(r'^tracks/$', views.track_list),
    url(r'^tracks/(?P<pk>[0-9]+)$', views.track_detail),
    url(r'^contests/$', views.contest_list),
    url(r'^contests/(?P<pk>[0-9]+)$', views.contest_detail),
    url(r'^userlevels/$', views.userlevel_list),
    url(r'^userlevels/(?P<pk>[0-9]+)$', views.userlevel_detail),
    url(r'^assignments/$', views.assignment_list),
    url(r'^assignments/(?P<pk>[0-9]+)$', views.assignment_detail),
    url(r'^recruiters/$', views.recruiter_list),
    url(r'^recruiters/(?P<pk>[0-9]+)$', views.recruiter_detail),
    url(r'^testassigns/$', views.testassign_list),
    url(r'^testassigns/(?P<pk>[0-9]+)$', views.testassign_detail),
    url(r'^detailedreports/$', views.detailedreport_list),
    url(r'^detailedreports/(?P<pk>[0-9]+)$', views.detailedreport_detail),
    url(r'^register/$', views.register , name = 'register'),
    url(r'^user_login/$',views.user_login, name='user_login')
]
