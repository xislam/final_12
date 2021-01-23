from django.urls import path, include
from django.views.generic import TemplateView

from accounts.views import signup, ProfileDetailView, UserProfileUpdateView, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UserProfileUpdateView.as_view(), name='profile'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    path('register/', signup, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]