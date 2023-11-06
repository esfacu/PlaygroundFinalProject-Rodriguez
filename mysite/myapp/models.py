from django.db import models

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
    
    def eliminar_task(request, task_title):
        task = Task.objects.get(title=task_title)
        task.delete()
    
    
class Developers(models.Model):
    name = models.CharField(max_length=200)
    edad = models.CharField(max_length=120)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + ' - ' + 'Trabajando en : ' + self.task.title
         
    #def __str__(self):
     #   return self.name