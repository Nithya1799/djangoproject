

from django import forms



#form definition

# class BookForm(forms.Form):
#     title=forms.CharField(max_length=100)
#     author=forms.CharField(max_length=100)
#     price=forms.IntegerField()
#     language=forms.CharField(max_length=100)
#     pages=forms.IntegerField()
#     image=forms.ImageField()

#Using ModelForm
from books.models import Book
class BookForm(forms.ModelForm):
    class Meta: #inner class used to give description about form structure
        model=Book
        #fields="__all__"
        #or
        fields=['title','author','price','language','pages','image']






