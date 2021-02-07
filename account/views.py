from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth import views, forms
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView

from .models import User
from .forms import ProfileForm


class LoginView(TemplateView):
    template_name = 'account/login.html'


class LogoutView(views.LogoutView):
    """
    Extends LogoutView to add logout message
    """

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Sampai jumpa di lain kesempatan :)',
                      extra_tags='success')
        return super().dispatch(request, *args, **kwargs)


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.info(self.request, 'Profile berhasil disimpan!',
                      extra_tags='success')
        return super().form_valid(form)


def authentication(request):
    return render(request, 'account/authentication.html')


def settings(request):
    return render(request, 'account/settings.html')