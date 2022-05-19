from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to='categories',
                              blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title



