from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.views.generic.base import View

from accounts.forms import UserRegistrationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('accounts:profile', kwargs={'pk': user.profile.pk}))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile-detail.html'


class ProfileUpdateView(View):
    template_name = 'profile.html'
