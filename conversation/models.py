from django.db import models
from item.models import Entambarotra
from django.contrib.auth.models import User


class Conversation(models.Model):
    item = models.ForeignKey(Entambarotra, related_name='conversations',on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='created_messages', on_delete=models.CASCADE)
    content = models.TextField()
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    