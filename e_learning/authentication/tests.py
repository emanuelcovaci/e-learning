from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegisterForm


# Create your tests here.


class AuthFormsTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username="user_test",
                                             email="smt@smt.com",
                                             password="top_secret")

    def test_valid_login_form(self):  # Login Form
        form_data = {'username': 'user_test', 'password': 'top_seret'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_form(self):  # Register Form invalid
        form_data = {'username': 'user_test', 'email': 'smt@smt.com',
                     'password': '1231', 'password2': '23232332daw'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_user_form(self):  # Register Form valid
        form_data = {'username': 'usertestvalid', 'email': 'sdwmt@gmail.com',
                     'password': 'aloha123', 'retypepassword': 'aloha123'}
        form = UserRegisterForm(data=form_data)
        print form.errors
        self.assertTrue(form.is_valid())

