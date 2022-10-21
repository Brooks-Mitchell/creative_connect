from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.test import TestCase
from rest_framework import status

# Create your tests here.

class UserTest(APITestCase):
  def setUp(self):
    self.test_user = User.objects.create_user('test_user', 'test@test.com', 'TestPassword9!')

    self.create_url = reverse('create-account')

  def test_create_user(self):
    data = {
      'username': 'TestUser',
      'email' : 'testemail@email.com',
      'password' : 'TESTpassWord9!'
    }

    response = self.client.post(self.create_url, data, format='json')

    self.assertEqual(User.objects.count(), 2)
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    self.assertEqual(response.data['username'], data['username'])
    self.assertEqual(response.data['email'], data['email'])
    self.assertFalse('password' in response.data)