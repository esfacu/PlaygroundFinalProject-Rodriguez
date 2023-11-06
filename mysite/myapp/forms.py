from django import forms
from .models import Project, Developers, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

class DevForm(forms.ModelForm):
    class Meta:
        model = Developers
        fields = ['name', 'edad', 'task']
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project','done', 'priority']