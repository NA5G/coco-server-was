# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post, Tag

@login_required
def index(request):
    context = {
        'title': "메인",
        'posts': Post.objects.filter(is_active=True)
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def tagged_posts(request, tag_name=""):
    context = {
        'title': '#%s' % (tag_name),
        'posts': Post.objects.filter(tags__name=tag_name, is_active=True)
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def users_posts(request, username=""):
    context = {
        'title': '@%s' % (username),
        'posts': Post.objects.filter(user__username=username, is_active=True)
    }

    return render(request, 'dashboard/index.html', context)
