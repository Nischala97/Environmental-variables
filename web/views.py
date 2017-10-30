'''from django.shortcuts import render'''
from django.http import HttpResponse

def index(request):
	return HttpResponse("Page is working")
# Create your views here.
