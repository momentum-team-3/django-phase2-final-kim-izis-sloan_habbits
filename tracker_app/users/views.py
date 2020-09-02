from django.shortcuts import render

# Create your views here.
""" These views implement a correctly configured set of user interactions. They are
    identical to the django buitlin views, but somewhat easier to customize.
"""
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
import django.contrib.auth as dj_auth
import django.contrib.auth.views as auth_views
from .models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank registration form .
        form = UserCreationForm()
    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('tracker_app:index')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)        



def signup(request):
    """ User account creation view.
    """
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = dj_auth.authenticate(username=username, password=raw_password)
            dj_auth.login(request, user)
            return redirect(to='notes/')

    else:
        form = forms.UserCreationForm()

    return render(request, 'users/create.html', {'form': form})


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    authentication_form = forms.AuthenticationForm


class LogoutView(auth_views.LogoutView):
    template_name = "users/logout.html"
    

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "users/change_password.html"
    form_class = forms.PasswordChangeForm


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "users/change_password_done.html"


class PasswordResetView(auth_views.PasswordResetView):
    template_name = "users/reset_password.html"
    email_template_name = "users/password_reset_email.html"
    form_class = forms.PasswordResetForm


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "users/reeset_password_done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "users/reset_password_confirm.html"
    form_class = forms.SetPasswordForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"