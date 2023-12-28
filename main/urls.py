"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from project.views import RegisterView,LoginView,LogoutView,TaskView,Taskedit,Taskdelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view(),name="register"),
    path('',LoginView.as_view(),name="Login"),
    path('logout/',LogoutView.as_view(),name="signout"),
    path('task/',TaskView.as_view(),name="home"),
    path('task/edit/<int:pk>',Taskedit.as_view(),name="edit"),
    path('task/delete/<int:pk>',Taskdelete.as_view(),name="delete")
]
