from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.BooleanField(default=True)
