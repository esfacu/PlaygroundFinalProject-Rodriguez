from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('form_project/', views.crear_proyecto),
    path('devs/', views.devs),
    path('form_dev/', views.crear_dev),
    path('form_task/', views.crear_task),
    path('buscar_task', views.buscar_task, name='buscar_task'),
    path('eliminar_task/<task_title>', views.eliminar_task, name="Delete"),
]