from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.write, name='write_post'),
    url(r'^(?P<post_id>\d+)$', views.single_post, name='single_post'),
    url(r'^(?P<post_id>\d+)/complete$', views.complete_deal, name='complete_deal')
]
