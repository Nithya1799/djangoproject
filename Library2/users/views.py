from django.shortcuts import render,redirect
from users.forms import SignupForm
from django.views import View
from users.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from users.models import User


from django.core.mail import send_mail



class Signup(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)
            user.is_active=False
            user.save()
            user.generate_otp()
            send_mail(
                "Django Auth OTP",
                user.otp,
                "nnthyaanithuu30@gmail.com",
                [user.email],
                fail_silently=False,
            )
            return redirect('users:otp')
        return render(request,'register.html',{'form':form_instance})


    def get(self,request):
        form_instance=SignupForm()
        return render(request,'register.html',{'form':form_instance})

class Login(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                return redirect('books:home')
            else:
                return redirect('users:login')
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')


from django.contrib import messages
class Otp(View):
    def post(self,request):
        otp=request.POST['o']
        try:
            u=User.objects.get(otp=otp)
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('users:login')
        except:
            messages.error(request,'Invalid OTP')
            return redirect('users:otp')
    def get(self,request):
        return render(request,'otp.html')