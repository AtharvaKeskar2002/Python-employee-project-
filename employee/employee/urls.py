"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from employeeapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('home',home,name="home"),
    path('elogin/',elogin,name='elogin'),
    path('alogin/',alogin,name='alogin'),
    path('singin/',signin,name='signin'),
    path('employeeform1/',employeeform1,name='employeeform1'),
    path('evalutionform/',evalutionform,name='evalutionform'),
    path('admindashboard/',admindashboard,name='admindashboard'),
    path('thankyou',thankyou,name='thankyou'),

]
