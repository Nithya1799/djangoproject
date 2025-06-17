"""
URL configuration for Library project.

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
from django.contrib import admin
from django.urls import path
from books import views
app_name="books"

urlpatterns = [
    path('',views.home,name="home"),
    path('addbook',views.addbook,name="addbook"),
    path('addbook1',views.addbook1,name="addbook1"),
    path('viewbook',views.viewbook,name="viewbook"),
    path('bookdetail/<int:i>',views.bookdetail,name="bookdetail"),
    path('deletebook/<int:i>',views.deletebook,name="deletebook"),
    path('editbook/<int:i>',views.editbook,name="editbook"),
    path('searchbook',views.searchbooks,name="searchbooks"),
    path('verify_otp',views.OtpVerificationView.as_view(),name="verify"),

]
