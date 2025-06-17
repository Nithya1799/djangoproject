from django.shortcuts import render,redirect

from app1.models import Movie
from django.urls import reverse_lazy
#listview
# def movielist(request):
#     m=Movie.objects.all()
#     return render(request,'movielist.html',{'movies':m})

from django.views.generic import ListView
class MovieList(ListView):
      model=Movie
      template_name = 'movielist.html'
      context_object_name='movies'



from app1.forms import MovieForm
# #Addmovie
# def addmovie(request):
#     if(request.method=="POST"):
#         form_instance=MovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist')
#     form_instance=MovieForm()
#     return render(request,'addmovie.html',{'form':form_instance})

from django.views.generic import CreateView
class AddMovie(CreateView):
    form_class=MovieForm
    template_name='addmovie.html'
    model=Movie
    success_url=reverse_lazy('movielist')



#DetailView
# def moviedetail(request,i):
#     m=Movie.objects.get(id=i)
#     return render(request,'moviedetail.html',{'movie':m})


from django.views.generic import DetailView
class MovieDetail(DetailView):
    model=Movie
    template_name='moviedetail.html'
    context_object_name='movie'



#DeleteView
# def deletemovie(request,i):
#     m=Movie.objects.get(id=i)
#     m.delete()
#     return redirect('movielist')

from django.views.generic import DeleteView
class DeleteMovie(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('movielist')




# def editmovie(request,i):
#     m=Movie.objects.get(id=i)
#     if (request.method == "POST"):
#         form_instance = MovieForm(request.POST, request.FILES,instance=m)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist')
#     form_instance=MovieForm(instance=m)
#     return render(request,'editmovie.html',{'form':form_instance})


from django.views.generic import UpdateView
class EditMovie(UpdateView):
    form_class=MovieForm
    template_name='editmovie.html'
    model=Movie
    success_url=reverse_lazy('movielist')
