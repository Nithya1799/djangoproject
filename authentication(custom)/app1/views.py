from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

# Create your views here.
class SignUpView(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
           # user=form_instance.save(commit=False)
           #  # user.set_password(raw_data)
           # user.set_password(form_instance.cleaned_data['password'])   #change the plaintext password
           # user.save()                                                           # format into encrpted format using django's
           #                                                                  # SHA alogithm so here we can call bilt-in function
           #
           form_instance.save()
           print('hello')
           return redirect('home')







    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login
class signinView(View):

    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            # authenticate ()returns user if all the user credintials are correct alse none
            if user:
            #starting session using current user
                login(request,user)
                # u=request.user
                # print(u)
                # print(u.username)
                # print(u.email)
                # print(u.first_name)

                return redirect('home')
            else:
                print("invalid user credentials")
                return redirect('signin')


    def get(self,request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

from django.contrib.auth import logout
class signoutView(View):
    def get (self,request):
        logout(request)#remove the user from current session
        return redirect('signin')

