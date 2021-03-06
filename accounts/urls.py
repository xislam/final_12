from django.urls import path, include
from django.views.generic import TemplateView

from accounts.views import signup, ProfileDetailView, UserProfileUpdateView

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UserProfileUpdateView.as_view(), name='profile'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    path('register/', signup, name='register'),
]