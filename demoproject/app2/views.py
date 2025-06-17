from django.shortcuts import render

def third(request):
    return render(request,'third.html')

def fourth(request):
    return render(request,'fourth.html')
