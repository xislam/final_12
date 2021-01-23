from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView


class UserListView(ListView):
    model = User
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.exclude(id=self.request.user.id)
        else:
            return User.objects.none()


def add_user_to_friends(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        request.user.profile.friends.add(user.profile)
        request.user.profile.save()
        return HttpResponse("hello world")
    else:
        return redirect(reverse('chat:user_list'))


def remove_user_from_friends(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        request.user.profile.friends.remove(user.profile)
        request.user.profile.save()
        return HttpResponse("hello world")
    else:
        return redirect(reverse('chat:user_list'))
