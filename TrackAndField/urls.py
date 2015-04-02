from django.conf.urls import patterns, include, url
from django.contrib import admin
from roster import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackAndField.views.home', name='home'),
    # url(r'^TrackAndField/', include('TrackAndField.foo.urls')),
    url(r'^hello-world/$', 'roster.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='roster_home'),
    url(r'^event/$', views.eventList, name='roster_event_list'),
    url(r'^athlete/(?P<team_pk>\d+)$', views.team_athlete_list, name='roster_athlete_list'),
    url(r'^event/(?P<pk>\d+)$', views.event, name='roster_event'),
    url(r'^team_athlete/(?P<pk>\d+)$', views.athlete, name='roster_athlete'),
    url(r'^team/$', views.teamList, name='roster_team_list'),
    url(r'^team/(?P<pk>\d+)$', views.team, name='roster_team')
)

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


  

