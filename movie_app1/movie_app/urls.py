"""
URL configuration for movie_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from threading import settrace

from django.contrib import admin
from django.urls import path
from movielist import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.movie_list,name="movie_list"),
    path('add_movie',views.add_movie,name="add_movie"),
    path('detail_view/<int:i>',views.detail_view,name="detail_view"),
    path('edit_view/<int:i>',views.edit_view,name="edit_view"),
    path('deletemovie/<int:i>', views.deletemovie, name="deletemovie"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

