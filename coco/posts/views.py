# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import WritePostForm
from models import Post, Auction

@login_required
def single_post(request, post_id=None):
    # TODO
    return HttpResponse(Post.objects.get(id=post_id).is_active)

@login_required
def complete_deal(request, post_id=None):
    # TODO
    auction = Auction.objects.get(post__id=post_id)
    auction.complete()
    return HttpResponse([auction.post.id, auction.post.is_active])

@login_required
def write(request):
    form = WritePostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = form.write(request)
        if post:
            # messages.success(request, '상품이 등록됐습니다.')
            return redirect('single_post', post_id=post.id)
        else:
            messages.success(request, '상품이 등록에 실패했습니다.')
            return redirect('/')

    return render(request, 'posts/write.html', {'form': form, 'message': 'hi'})
