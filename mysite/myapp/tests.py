from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project, Task, Developers, Avatar

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.project = Project.objects.create(name='Test Project')
        self.task = Task.objects.create(title='Test Task', description='Task description', project=self.project)
        self.developer = Developers.objects.create(name='Test Developer', edad='25', task=self.task)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CODERHOUSE - CURSO PYTHON FLEX')

    def test_project_list_view(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_devs_list_view(self):
        response = self.client.get(reverse('devs-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Developer')

    def test_editarPerfil_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('EditarPerfil'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit Profile')

class TestModels(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name='Test Project')
        self.task = Task.objects.create(title='Test Task', description='Task description', project=self.project)
        self.developer = Developers.objects.create(name='Test Developer', edad='25', task=self.task)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.avatar = Avatar.objects.create(user=self.user, imagen='path/to/test/image.jpg')

    def test_project_model(self):
        self.assertEqual(str(self.project), 'Test Project')

    def test_task_model(self):
        self.assertEqual(str(self.task), 'Test Task - Test Project')

    def test_developer_model(self):
        self.assertEqual(str(self.developer), 'Test Developer - Trabajando en : Test Task')

    def test_avatar_model(self):
        self.assertEqual(str(self.avatar), f"{self.user} - path/to/test/image.jpg")
