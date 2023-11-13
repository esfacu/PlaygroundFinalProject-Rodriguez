from django.urls import path
from . import views
from .views import *
#Para logout
from django.contrib.auth.views import LogoutView

#PARA LAS IMAGENES
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    #path('projects/', views.projects),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    #path('tasks/', views.tasks),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    #path('tasks/<pk>/task_confirm_delete/', TaskDeleteView.as_view(), name='task-confirm-delete'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('form_project/', views.crear_proyecto),
    #path('devs/', views.devs),
    path('devs/', DevsListView.as_view(), name='devs-list'),
    path('form_dev/', views.crear_dev),
    path('delete_dev/<int:pk>/', DevDeleteView.as_view(),name="dev_confirm_delete"),
    #task
    path('form_task/', views.crear_task),
    path('tasks/<int:pk>/update_task/', views.TaskUpdateView.as_view(), name='update_task'),
    path('buscar_task', views.buscar_task, name='buscar_task'),
    
    #login y logout
    path('login/', views.login_request, name='Login'),
    path('', views.login_request, name='Login'),
    path('registro/', views.register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html')),
    
    #users
    path('userEdit/', views.editarPerfil, name="EditarPerfil"),
    path('editPassword/', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"), 
    
    #POLICY
    path('contact/', views.contact, name="contact"),
    path('privacy/', views.privacy, name="privacy"),
    path('terms/', views.terms, name="terms"),  
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)