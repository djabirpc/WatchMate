from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import response, status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            'username':'manel',
            'email':'manel@gmail.com',
            'password':'Manel123',
            'password2':'Manel123'
        }
        response = self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)