from django.contrib.auth.models import User
from django.db import models
from categories.models import Category


class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    details = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
