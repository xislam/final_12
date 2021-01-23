from django.urls import path

from chat.views import UserListView

app_name = 'chat'

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
]