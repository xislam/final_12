from django.urls import path

from chat.views import UserListView, add_user_to_friends, remove_user_from_friends, send_message, chat_form, chat_room

app_name = 'chat'

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user/add/<int:user_id>/', add_user_to_friends, name='add'),
    path('user/remove/<int:user_id>/', remove_user_from_friends, name='remove'),
    path('send-message/<int:user_id>/', send_message, name='send'),
    path('chat-form/<int:user_id>/', chat_form),
    path('chat-room/', chat_room, name='chat_room'),
]