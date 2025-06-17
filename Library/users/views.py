from django.shortcuts import render,redirect
from django.views import View
from users.forms import SignupForm
from users.forms import LoginForm
from django.contrib.auth import authenticate,login
# def register(request):
#     return render(request,'register.html',)
# def login(request):
#     return render(request,'login.html',)
def logout(request):
    return render(request,'logout.html',)

class RegisterView(View):
    def get(self, request):
        form_instance=SignupForm()
        return render(request,'register.html',{'form':form_instance})
    def post(self,request):
         form_instance=SignupForm(request.POST)
         if form_instance.is_valid():
             user=form_instance.save(commit=False)
             user.set_password(form_instance.cleaned_data['password'])
             user.save()
             return redirect('books:home')
class LoginView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                u=request.user
                print(u.username)
                print(u.email)
                print(u.last_name)
                return redirect('books:home')
            else:
                print('invalid user credential')
                return redirect('user:login')