"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from my_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',Userreigistarationview.as_view(),name='signup'),
    path('Login/',Loginview.as_view(),name='login'),
    path('logout/',Logoutview.as_view(),name='logout'),
    path('addtask/create/',Addtaskview.as_view(),name='create'),
    path('task/list/',Taskreadview.as_view(),name='tasklist'),
    path('update/<int:pk>',Taskupdate.as_view(),name="update"),
    path('delete/<int:pk>',Taskdelete.as_view(),name='delete'),
    path('read/<int:pk>',Taskdetails.as_view(),name='detail'),
    path('edit/<int:pk>',Taskedit.as_view(),name='edit'),
    path('forgot/',Forgotpassword.as_view(),name='forgot'),
    path('verifyotp/',Otpverifyview.as_view(),name='otpverify'),
    path('reset/',Resetpassword.as_view(),name='reset'),
    path('filter/',Taskfilterview.as_view(),name='filter'),
    path('',Index.as_view(),name="indexx")
]
