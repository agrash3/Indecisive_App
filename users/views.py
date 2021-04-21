# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def signup(response):
    form = UserCreationForm()
    return render(response, 'signup.html', {'form':form})


class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'

class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
