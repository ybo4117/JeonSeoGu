from django.db import models

class BlogData(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()