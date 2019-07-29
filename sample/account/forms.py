from django import forms
from .models import User


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userId', 'password', 'nick']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginUserForm(forms.Form):
    userId = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())

    @property
    def clean_userId(self):
        if self.userId != None or self.userId != '':
            return True
        return False
