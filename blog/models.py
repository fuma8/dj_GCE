from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
# Create your models here.
