# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search/tags/(?P<tag_name>(.)+)/$', views.tagged_posts, name='tagged_post'),
    url(r'^search/users/(?P<username>(.)+)/$', views.users_posts, name='users_post'),
]
