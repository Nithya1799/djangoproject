

from django import forms
from django.forms import PasswordInput


class AdditionForm(forms.Form):  #form structure definition
    number1=forms.IntegerField()
    number2=forms.IntegerField()
class Factform(forms.Form):
    number1=forms.IntegerField()
class BmiForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()

class SignupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    email=forms.EmailField()
    gender_choices=[('male',"Male"),('female',"Female")]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    role_choices=[('admin','Admin'),('student','Student')]
    role=forms.ChoiceField(choices=role_choices)


    # <select>
    # <option value="male">Male</option>
    # <option value="female">Female</option>
    # </select>

class CalorieForm(forms.Form):


    weight=forms.IntegerField()
    # <input type="number" class="form-control">
    height=forms.IntegerField()

    age=forms.IntegerField()
    gender_choices = [('male', "Male"), ('female', "Female")]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

    activity_choices=[(1.2,'sedentary'),
                      (1.375,'lightly active'),
                      (1.55,'moderately active'),
                      (1.725,'very active'),
                      (1.9,'extra active')]

    activity_level=forms.ChoiceField(choices=activity_choices)






