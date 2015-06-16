from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
    # TODO
    return HttpResponse('TODO')
