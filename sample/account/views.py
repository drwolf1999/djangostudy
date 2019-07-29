from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from .utils import Utils
from .models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/web')
    else:
        form = RegisterUserForm()
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        print(form)
        if form.is_valid() and Utils.isValidLoginInformation(form):
            request.session['userId'] = form.data['userId']
            request.session['password'] = form.data['password']
            return redirect('/web')
        else:
            context = {
                'form': form,
                'error': True,
            }
            return render(request, 'account/login.html', context)
    else:
        form = LoginUserForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)


def logout(request):
    request.session.pop('userId', None)
    request.session.pop('password', None)
    return redirect('/web')
