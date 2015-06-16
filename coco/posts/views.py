from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def post_list(request):
	# write about make post list

	return HttpResponse("hello post list")

def post(request):
	# write about make post
	
	return HttpResponse("hello post")

def write(request):
	pass