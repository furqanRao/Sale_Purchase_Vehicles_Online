from django.conf.urls import url, include
from vehicles_app import views
from .views import *

# template tagging
app_name = 'vehicles_app'

urlpatterns = [
    url(r'^cars/$', views.cars, name='cars'),
    url(r'^bikes/$', views.bikes, name='bikes'),
    url(r'^trucks/$', views.trucks, name='trucks'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^addfile/$', views.addfile, name='addfile'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.FileDelete.as_view(), name='file-delete'),
    url(r'^(?P<post_id>[0-9]+)/data/$', views.data, name='data'),
    url(r'^(?P<post_id>[0-9]+)/update_post/$', views.update_post, name='update_post'),
    url(r'^myposts/$', views.myposts, name='myposts'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^frequently_searched/$', views.frequently_searched, name='frequently_searched'),
]
