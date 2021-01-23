from django.urls import path

from chat.views import UserListView, add_user_to_friends, remove_user_from_friends

app_name = 'chat'

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('user/add/<int:user_id>/', add_user_to_friends, name='add'),
    path('user/remove/<int:user_id>/', remove_user_from_friends, name='remove')
]