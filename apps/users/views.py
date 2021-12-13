from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as django_auth_login,
    logout as django_auth_logout,
    authenticate
)

from apps.users import forms


def login(request):
    form = forms.LoginForm()

    if request.method == "POST":
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )

            if user:
                django_auth_login(request, user)
                return redirect(request.GET.get('next', '/'))

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)


def logout(request):
    django_auth_logout(request)
    return redirect('users:login')
