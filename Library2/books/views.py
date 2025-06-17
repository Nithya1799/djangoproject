from django.shortcuts import render, redirect

from books.forms import AddbookForm
from django.views import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
     return render(request, 'home.html')



class AddbookView1(View):
    def get(self,request,*args,**kwargs):
        form_instance = AddbookForm()
        return render(request, 'add_books.html', {'forms': form_instance})
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        # print(request.FILES)
        form_instance = AddbookForm(request.POST, request.FILES)

        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:view')
        # return render(request,'add_books.html')





from books.models import Book


# user defined form
class AddbookView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'add_books1.html')
    def post(self,request,*args,**kwargs):

        # print(request.POST)
        # print(request.FILES)
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i = request.FILES['i']
        b = Book.objects.create(title=t, author=a, price=p, pages=pa, language=l, image=i)
        b.save()
        # return render(request,'add_books1.html')
        return redirect('books:view')



class ViewbookView(View):
    def get(self,request,*args,**kwargs):
     b = Book.objects.all()
     print(b)
     return render(request, 'view_book.html', {'book': b})

class DetailView(View):
  def get(self,request, i):
    b = Book.objects.get(id=i)
    return render(request, 'detail.html', {'book': b})

class Edit(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = AddbookForm(instance=b)
        return render(request, 'edit.html', {'forms': form_instance})
    def post(self,request, i):
        b = Book.objects.get(id=i)

        form_instance = AddbookForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:view')


class Delete(View):
  def get(self,request, i):
    Book.objects.get(id=i).delete()
    return redirect('books:view')


from django.db.models import Q

class Search(View):
 def get(self,request):
      return render(request, 'search.html')
 def post(self,request):
        data = request.POST['s']
        print(data)
        b = Book.objects.filter(Q(title__icontains=data) | Q(author__icontains=data) | Q(language__icontains=data))
        #lookups--> (filename__lookup)
        print(b)
        return render(request, 'search.html',{'book':b})
