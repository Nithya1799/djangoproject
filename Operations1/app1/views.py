from django.shortcuts import render

#Addition
from app1.forms import AdditionForm
def addition(request):
        if(request.method=="POST"):
            print(request.POST)
            return render(request,'addition.html')


        #GET Request
        form_instance=AdditionForm()  #empty form object
        return render(request,'addition.html',{'form':form_instance})



def fact(request):

    return render(request,'factorial.html')


def bmi(request):


    return render(request,'bmi.html')

from app1.forms import SignupForm
def signup(request):

    if request.method=="GET":
        form_instance=SignupForm()  #form instance
        return render(request,'signup.html',{'form':form_instance})


from app1.forms import CalorieForm
def calorie(request):

    if request.method=="POST":#After form submission
        print(request.POST) #submitted data

        #creating form object using data submitted by user
        form_instance=CalorieForm(request.POST)

        #Checks the validity of data using is_valid()
        if form_instance.is_valid():

            #Accessing the cleaned data after validation
            data=form_instance.cleaned_data
            weight=data['weight']
            height=data['height']
            print(type('height'))
            age=data['age']
            gender=data['gender']
            activity_level=data['activity_level']
            print(type(activity_level))
            print(weight,height,age,gender,activity_level)

            if(gender=="male"):
                 bmr=10 * weight + 6.25 * height- 5 * age+ 5 # for (man)

            else:

                bmr= 10 * weight + 6.25 * height- 5 * age- 161 # for ​(woman)
            c=bmr*float(activity_level)
            print(c)


        return render(request,'calorie.html',{'form':form_instance,'result':c})

    if request.method=="GET":
        form_instance=CalorieForm()
        return render(request,'calorie.html',{'form':form_instance})