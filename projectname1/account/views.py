from django.shortcuts import render, redirect
from .models import Account
from .forms import RegisterForm, LoginForm
from .utils import Util
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app')
    else:
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() and Util.isValidLogin(form):
            request.session['userId'] = form.data['userId']
            return redirect('/app')
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'account/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)

def logout(request):
    request.session.pop('userId', None)
    return redirect('/app')