# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'users.views.sign_up'),
    url(r'^signup/$', 'users.views.sign_up', name='sign_up'),
    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^logout/$', 'users.views.logout'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^posts/', include('posts.urls')),
] + static('static_files', document_root=settings.MEDIA_ROOT)
