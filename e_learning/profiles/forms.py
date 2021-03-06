from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from authentication.models import Account


class UserEdit(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserEdit, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email) and self.user.email != email:
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count() and \
           self.user.username != user_name:
            raise forms.ValidationError("This username already exists")
        return user_name


class AccountEdit(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['profile_image']
