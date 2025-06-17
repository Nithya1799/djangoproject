from django import forms
# class AddmovieForm(forms.Form):
#     Movie_Name=forms.CharField(max_length=70)
#     Director_Name=forms.CharField(max_length=70)
#     Description=forms.CharField(widget=forms.Textarea)
#     Language_choices = [('english', 'English'), ('french', 'French'), ('malayalam', 'Malayalam'), ('hindi', 'Hindi'),('tamil','Tamil'),('kannada','Kannada')]
#     Language = forms.ChoiceField(choices=Language_choices)
#     Year=forms.IntegerField()
#     Image=forms.ImageField()

from  movielist.models import Movies
class AddmovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'director_name', 'description', 'language', 'Year', 'image']

