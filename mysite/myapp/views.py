from django.http import HttpResponse
from .models import Project, Task, Developers, CustomUserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm, DevForm, TaskForm, UserEditForm
from django.contrib import messages
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    title = 'CODERHOUSE - CURSO PYTHON FLEX'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request):
    return HttpResponse(request)

def about(request):
    username = 'Facu'
    return render(request, 'about.html', {
    })
#PRIMERO TRAE LISTA COMO FUNCION LUEGO COMO CLASE DE LISTVIEW
#def projects(request):
    #projects = list(Project.objects.values())
    #projects = Project.objects.all()
    #return render(request, 'projects/projects.html', {
     #   'projects' : projects
    #})
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    
#task como funcion primero y luego como clase
#def tasks(request):
  #  #task = get_object_or_404(Task, id=id)
    #task = Task.objects.all()
    #return render(request, 'tasks/tasks.html', {
    #    'task': task
    #})
    
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('index')
    
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    fields = ['title', 'description', 'project','done', 'priority']
    success_url = '/'
    
    
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = ProjectForm()
    
    return render(request, 'projects/crear_proyecto.html', {'form': form}) 


#def devs(request):
  #  #projects = list(Project.objects.values())
#    developers = Developers.objects.all()
 #   return render(request, 'devs/developers.html', {
  #      'developers' : developers
   # })

class DevsListView(ListView):
    model = Developers
    template_name = 'devs/developers.html'
    context_object_name = 'developers'
    
def crear_dev(request):
    if request.method == 'POST':
        form = DevForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = DevForm()
    
    return render(request, 'devs/agregar_dev.html', {'form': form}) 

def crear_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/')  # Redirige a la lista de proyectos
    else:
        form = TaskForm()
    
    return render(request, 'tasks/agregar_task.html', {'form': form}) 

def buscar_task(request):
    query = request.GET.get('q')
    if query:
        tareas = Task.objects.filter(title__icontains=query)
        if not tareas:
            messages.info(request, 'No se encontraron tareas con ese nombre.')
    else:
        tareas = Task.objects.all()
    return render(request,'tasks/tasks.html', {'tareas': tareas, 'query': query})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            
            return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})
    
  


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirige a donde quieras después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/registro.html', {'form': form})
        
        
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=request.user)
        
        if miFormulario.is_valid():
            miFormulario.save()
            
            return render(request, "index.html")
    
    else:
        miFormulario = UserEditForm(instance=request.user)
        
    return render(request, "users/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})