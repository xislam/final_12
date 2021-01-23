from django.db import models


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sender_messages')
    receiver = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='receiver_messages')
    created = models.DateTimeField(auto_now_add=True)
