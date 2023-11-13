from django import forms
from .models import Project, Developers, Task, User
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

class DevForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, label='Imagen')
    
    class Meta:
        model = Developers
        fields = ['name', 'edad', 'task', 'imagen']
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project','done', 'priority']
        
        
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Enter Mail: ")
    last_name = forms.CharField(label="Surrname")
    first_name = forms.CharField(label="Name")
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields =  ['email', 'last_name', 'first_name', 'imagen']