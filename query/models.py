from django.db import models
from django.conf import settings


class UserQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.user} at {self.created_at}"
