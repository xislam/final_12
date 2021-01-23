from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/avatars/%Y/%m/%d', null=True, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    friends = models.ManyToManyField("self", blank=True)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={
            'pk': self.pk
        })