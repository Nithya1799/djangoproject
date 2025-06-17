from django import forms


# class AddbookForm(forms.Form):
#     title = forms.CharField()
#     author = forms.CharField()
#     price = forms.FloatField()
#     pages = forms.IntegerField()
#     language = forms.CharField()
#     image = forms.ImageField()

from books.models import Book
class AddbookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"