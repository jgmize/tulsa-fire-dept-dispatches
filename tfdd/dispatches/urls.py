from django.conf.urls import url, patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    'dispatches.views',

    url(r'^unit_select/','unit_select'),
    url(r'^send_text/','send_text'),
    url(r'^follow/(?P<unit_id>.*)/(?P<channel>.*)/(?P<state>.*)/$', 'follow_unit',
        name='follow_unit'),
    url(r'^post/$', 'post', name='dispatch_post'),
    url(r'^register/$', 'register', name='dispatches_register'),
    url(r'^login/$', direct_to_template, {'template': 'login.html'}, name='login'),
    url(r'^following/$', 'following', name='following'),
    url(r'^settings/$', direct_to_template, {'template': 'settings.html'}, name='settings'),
    url(r'^$', 'index', name='dispatches'),
)
