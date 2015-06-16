from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post/$', views.post, name='post'),
    url(r'^posts/new$', views.write, name='write_post')
]