from django.http import HttpResponse
from .models import Project, Task, Developers
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm, DevForm, TaskForm
from django.contrib import messages

# Create your views here.
def index(request):
    title = 'Django Course'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello World %s</h1>" %username)

def about(request):
    username = 'Facu'
    return render(request, 'about.html', {
        'username' : username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    return render(request, 'tasks.html', {
        'task': task
    })
    
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = ProjectForm()
    
    return render(request, 'crear_proyecto.html', {'form': form}) 


def devs(request):
    #projects = list(Project.objects.values())
    developers = Developers.objects.all()
    return render(request, 'developers.html', {
        'developers' : developers
    })
    
def crear_dev(request):
    if request.method == 'POST':
        form = DevForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = DevForm()
    
    return render(request, 'agregar_dev.html', {'form': form}) 

def crear_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = TaskForm()
    
    return render(request, 'agregar_task.html', {'form': form}) 

def buscar_task(request):
    query = request.GET.get('q')
    if query:
        tareas = Task.objects.filter(title__icontains=query)
        if not tareas:
            messages.info(request, 'No se encontraron tareas con ese nombre.')
    else:
        tareas = Task.objects.all()
    return render(request,'tasks.html', {'tareas': tareas, 'query': query})