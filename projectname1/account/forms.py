from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['userId', 'password', 'nick']
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    userId = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())
    @property
    def clean_userId(self):
        if self.userId == None or self.userId == '':
            return False
        return True