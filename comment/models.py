from django.contrib.auth.models import User
from django.db import models
from news.models import News


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.BooleanField(default=True)
