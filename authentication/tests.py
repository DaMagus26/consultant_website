from django.test import TestCase
from django.urls import reverse
from .models import User
from django.contrib.auth import get_user_model, authenticate


class UserAuthTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpassword123'))
        self.assertTrue(self.user.is_active)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_valid_login(self):
        self.client.login(email='test@example.com', password='testpassword123')
        response = self.client.get(reverse('home'))  # replace 'home' with your actual home page
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        self.client.login(email='test@example.com', password='wrongpassword')
        response = self.client.get(reverse('home'))
        self.assertNotEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(email='test@example.com', password='testpassword123')
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertNotEqual(response.context['user'], self.user)

    def test_valid_signup(self):
        response = self.client.post(reverse('signup'), {
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Assuming redirection after successful signup
        new_user = get_user_model().objects.get(email='newuser@example.com')
        self.assertTrue(new_user.check_password('newpassword123'))

    def test_invalid_signup(self):
        response = self.client.post(reverse('signup'), {
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)  # Stays on the same page due to form error

    def test_user_authentication(self):
        user = authenticate(email='test@example.com', password='testpassword123')
        self.assertIsNotNone(user)

    def test_user_authentication_failure(self):
        user = authenticate(email='test@example.com', password='wrongpassword')
        self.assertIsNone(user)
