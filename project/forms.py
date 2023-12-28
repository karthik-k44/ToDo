from django import forms 
from django.contrib.auth.models import User
from project.models import Task

class register(forms.ModelForm):
    class Meta:
        model = User
        fields=["username","password","first_name","last_name","email"]
        
class Login(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)

class TaskForm (forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["name"]
