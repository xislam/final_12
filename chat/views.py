from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView

from chat.forms import MessageForm


class UserListView(ListView):
    model = User
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.exclude(id=self.request.user.id)
        else:
            return User.objects.all()


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


def send_message(request, user_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        message = form.save(commit=False)
        message.sender = request.user
        receiver = User.objects.get(id=user_id)
        message.receiver = receiver
        message.save()
        return HttpResponseRedirect(reverse("chat:chat_room"))


def chat_form(request, user_id):
    if request.is_ajax():
        queryset = User.objects.filter(id=user_id)
        if queryset.exists():
            user = queryset.first()
            form = MessageForm()
            html = render_to_string("chat-form.html", {"user": user, "form": form}, request=request)
            return HttpResponse(html)
    else:
        return HttpResponseRedirect(reverse("chat:user_list"))


def chat_room(request):
    context = {}
    s_messages = request.user.sender_messages.all()
    r_messages = request.user.receiver_messages.all()
    context["s_messages"] = s_messages
    context["r_messages"] = r_messages
    return render(request, 'chat.html', context)
