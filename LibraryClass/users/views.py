from django.shortcuts import render

#Register
def register(request):
    return render(request,'register.html')
#login
def login(request):
    return render(request,'login.html')
#logout
def logout(request):
    return render(request,'logout.html')