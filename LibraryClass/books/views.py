from tkinter import image_names

from django.shortcuts import render,redirect

#Home
# def home(request):
#     return render(request,'home.html')

from django.views import View
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')


#Addbook
#User Defined Form View
from books.models import Book
# def addbook(request):
#     if(request.method=="POST"):
#         # print(request.POST)
#         # print(request.FILES)
#         #Accessing data from submitted form using request.POST
#         t=request.POST['t']
#         a=request.POST['a']
#         n=request.POST['n']
#         l=request.POST['l']
#         p=request.POST['p']
#         i=request.FILES['i']
#         #
#         # #Modelclassname.objects.create(field1=value1,field2=value2.....)
#         # #Creating a new object/record inside Model Book
#         b=Book.objects.create(title=t,author=a,price=n,language=l,pages=p,image=i)
#         b.save() #Saves the record
#         return redirect('books:viewbook')
#     return render(request,'addbook.html')

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addbook.html')

    def post(self,request,*args,**kwargs):
        #print(request.POST)
        # print(request.FILES)
        #Accessing data from submitted form using request.POST
        t=request.POST['t']
        a=request.POST['a']
        n=request.POST['n']
        l=request.POST['l']
        p=request.POST['p']
        i=request.FILES['i']
        #
        # #Modelclassname.objects.create(field1=value1,field2=value2.....)
        # #Creating a new object/record inside Model Book
        b=Book.objects.create(title=t,author=a,price=n,language=l,pages=p,image=i)
        b.save() #Saves the record
        return redirect('books:viewbook')
#Built in form View
from books.forms import BookForm
# def addbook1(request):
#     if(request.method=="POST"):
#         # print(request.POST)
#         # print(request.FILES)
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # data=form_instance.cleaned_data
#             # print(data)
#             # t=data['title']
#             # a=data['author']
#             # n=data['price']
#             # l=data['language']
#             # p=data['pages']
#             # b=Book.objects.create(title=form_instance.cleaned_data['title'],
#             #                       author=form_instance.cleaned_data['author'],
#             #                       price=form_instance.cleaned_data['price'],
#             #                       language=form_instance.cleaned_data['language'],
#             #                       pages=form_instance.cleaned_data['pages'],
#             #                       image=form_instance.cleaned_data['image'])
#
#             # b.save()
#             form_instance.save()
#             #redirect(pathname)
#
#         return redirect('books:viewbook')
#     if(request.method=="GET"):
#         form_instance=BookForm()
#         return render(request,'addbook1.html',{'form':form_instance})

class AddBookView1(View):
    def get(self,request,*args,**kwargs):
        form_instance = BookForm()
        return render(request,'addbook1.html',{'form':form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')
#Viewbook
# def viewbook(request):
#     b=Book.objects.all() #Reads all records(all objects) from Model Book.It returns a queryset
#       #it represents a sequence of objects
#     return render(request,'viewbook.html',{'books':b})

class ViewBook(View):
    def get(self,request,*args,**kwargs):
        b=Book.objects.all() #Reads all records(all objects) from Model Book.It returns a queryset
        #it represents a sequence of objects
        return render(request,'viewbook.html',{'books':b})

#Detail View
# def bookdetail(request,i):
#     print(i)
#     b=Book.objects.get(id=i)
#     return render(request,'detail.html',{'book':b})

class BookDetailView(View):
    def get(self,request,i):

        b=Book.objects.get(id=i)
        return render(request,'detail.html',{'book':b})




#Edit View
# def editbook(request,i):
#     b = Book.objects.get(id=i)
#     if(request.method=="POST"):
#         form_instance=BookForm(request.POST,request.FILES,instance=b)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('books:viewbook')
#
#
#     form_instance=BookForm(instance=b)
#     return render(request,'editbook.html',{'form':form_instance})


class EditBookView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        return render(request,'editbook.html',{'form':form_instance})

    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
                form_instance.save()
                return redirect('books:viewbook')


#Delete View
# def deletebook(request,i):
#     b=Book.objects.get(id=i)
#     b.delete()
#     return redirect('books:viewbook')

class DeleteView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbook')

#Search View

from django.db.models import Q
# def searchbooks(request):
#     if(request.method=="POST"):
#         print('hello')
#         data=request.POST['q']
#         print(data)
#         b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) |Q(language__contains=data))
#         #Filter condition -To read two or more records from a table
#         #Qobject -To use logical and/or/not syntax in ORM Queries
#         #Django lookups
#         #(filedname__lookup eg:age__gt,age__lt,age__gte,age__lte,title__contains,title__icontains)
#         print(b)
#         context={'book':b}
#         return render(request,'search.html',context)
#
#
#     return render(request,'search.html')

class SearchView(View):
    def get(self,request):
        return render(request, 'search.html')
    def post(self,request):
        data = request.POST['q']
        print(data)
        b = Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        # Filter condition -To read two or more records from a table
        # Qobject -To use logical and/or/not syntax in ORM Queries
        # Django lookups
        # (filedname__lookup eg:age__gt,age__lt,age__gte,age__lte,title__contains,title__icontains)
        print(b)
        context = {'book': b}
        return render(request, 'search.html', context)





