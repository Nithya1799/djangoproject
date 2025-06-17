from django.shortcuts import render
from django.http import HttpResponse
#Home View
def home(request):
                  # return HttpResponse("Welcome to home")

    context={'name':'Ananthan','age':25,'place':'klm'}
    return render(request,'home.html',context)


#First View
def first(request):
                  # return HttpResponse("First Page")
   return render(request,'first.html')


#Second View
def second(request):
                  # return HttpResponse("Second Page")
    return render(request,'second.html')
