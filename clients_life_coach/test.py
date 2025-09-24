from django.test import TestCase
from django.urls import reverse
from .models import Client

class ClientModelTests(TestCase):
    def test_create_client(self):
        c = Client.objects.create(first_name='Test', last_name='User', email='test@example.com')
        self.assertEqual(str(c), 'Test User <test@example.com>')

class ClientViewsTests(TestCase):
    def test_list_view(self):
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        response = self.client.post(reverse('client_add'), {
            'first_name': 'New', 'last_name': 'Client', 'email': 'new@example.com'
        })
        self.assertEqual(response.status_code, 302)  # redirect on success
