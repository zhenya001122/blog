from django.db import models


class Message(models.Model):
    action = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    message = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
