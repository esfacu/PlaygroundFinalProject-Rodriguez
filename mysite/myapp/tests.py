from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.models import User

from models import Developers, Task, Project

# Create your tests here.

class RegistrarTestCase(TestCase):
    def setUp(self):
        self.developer = Developers.objects.create(name="Juan", edad="28")
        self.url = reverse('DevDeleteView', args=[self.developer.name])
    
    def test_eliminar_developer(self):
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 200)
        
        self.assertTemplateUsed(respuesta, 'devs/developers.html')
        self.assertQuerySetEqual(Developers.objects.all(), [])