from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

PRIORIDAD_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]   
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=5, choices=PRIORIDAD_CHOICES,  default='baja')  # Establece 'baja' como valor predeterminado)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name
    
    
class Developers(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=120)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='developers', null=True, blank=True)
    
    def __str__(self):
        return self.name + ' - ' + 'Trabajando en : ' + self.task.title

         
 
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Deshabilita las etiquetas de ayuda para los campos del formulario
        for field_name, field in self.fields.items():
            field.help_text = None
            
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"