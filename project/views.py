from django.shortcuts import render,redirect
from django.views.generic import View 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from project.forms import register,Login,TaskForm 
from project.models import Task
from django.contrib import messages 
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('Login')
        else:
            return fn(request,*args, **kwargs)
    return wrapper

def mylogin(fn):
    def wrapper(request,*args, **kwargs):
        id=kwargs.get(pk)
        obj=Task.objects.filter(id=id)
        if obj.user != request.user:
            return redirect("login")
        else:
            return fn(request,*args, **kwargs)
    return wrapper

class RegisterView(View):
    def get(self, request):
        form = register()
        return render(request, "reg.html", {"form":form})
    
    def post(self, request):
        form=register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"added successfully")
            
        form=register()
        return redirect("login")
        
class LoginView(View):
    def get(self,request,*args, **kwargs):
        form=Login()
        return render(request, "login.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=Login(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("Username")
            pwd=form.cleaned_data.get("Password")
            print(u_name, pwd)
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valid creds")
                login(request,user_obj)
                return redirect("home")
            else:
                print("invalid creds")
        else:
            print("...")
        return render(request,"login.html",{"form":form})

decs=[signin_required,mylogin]
@method_decorator(decs, name="dispatch")
class TaskView(View):
    def get(self,request):
        form=TaskForm()
        data=Task.objects.filter(user=request.user).order_by('complete')
        return render(request, "task.html", {"form":form,"data":data})
    def post(self,request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        data=Task.objects.filter(user=request.user)
        return render(request, "task.html", {"form":form,"data":data})

class Taskedit(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).update(complete=True)
        return redirect("home")
    
class Taskdelete(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).delete()
        return redirect("home")
    
class LogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect ("Login")
    
    
    