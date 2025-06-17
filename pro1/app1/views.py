from django.shortcuts import render

from django.http import HttpResponse



#Home View
def home(request):

    return HttpResponse("Django")

#index View
def index(request):
    return HttpResponse("Index Page")
