from django.http import HttpResponse
from .models import Project, Task, Developers, CustomUserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm, DevForm, TaskForm, UserEditForm
from django.contrib import messages
from django.views.generic import ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.views import View

  

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
    
def contact(request):
    return render(request, 'policy/contact.html', {
    })
def privacy(request):
    return render(request, 'policy/privacy.html', {
    })
def terms(request):
    return render(request, 'policy/terms.html', {
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
    
class TaskDeleteView(PermissionRequiredMixin ,DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    permission_required = 'myapp.delete_task'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
      
class DevDeleteView(PermissionRequiredMixin ,DeleteView):
    model = Developers
    template_name = 'devs/devs_confirm_delete.html'
    success_url = reverse_lazy('index')
    permission_required = 'myapp.delete_developers'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
    
class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/projects_confirm_delete.html'
    success_url = reverse_lazy('project-list')
    permission_required = 'myapp.delete_project'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    fields = ['title', 'description', 'project','done', 'priority']
    success_url = reverse_lazy('task-list')
    permission_required = 'myapp.update_task'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
class ProjectUpdateView(PermissionRequiredMixin,UpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    fields = ['name']
    success_url = reverse_lazy('project-list')
    permission_required = 'myapp.update_project'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
class DevsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Developers
    template_name = 'devs/update_devs.html'
    form_class = DevForm
    def form_valid(self, form):
        # Actualiza la imagen solo si se proporciona una nueva imagen
        if form.cleaned_data['imagen']:
            # Elimina la imagen antigua antes de guardar la nueva
            old_imagen = self.get_object().imagen
            if old_imagen:
                old_imagen.delete(save=False)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('devs-list')
    
    permission_required = 'myapp.update_developers'
    permission_denied_message = 'No estas autorizado'
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return render(self.request, 'errores/403.html', status=403)
    
    
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('index')  # Redirige a la lista de proyectos
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
        form = DevForm(request.POST, request.FILES)  #  `request.FILES` para manejar archivos
        if form.is_valid():
            form.save()
            return redirect('/devs')
    else:
        form = DevForm()

    return render(request, 'devs/agregar_dev.html', {'form': form}) 

def crear_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proyecto en la base de datos
            return redirect('/tasks')  # Redirige a la lista de proyectos
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
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
                
            miFormulario.save()
            return render(request, "index.html")
    
    else:
        miFormulario = UserEditForm(instance=request.user)
        
    return render(request, "users/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editPassword.html"
    success_url = reverse_lazy('EditarPerfil')
    
