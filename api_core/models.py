from django.db import models

class NewsStory(models.Model):
  title = models.CharField(max_length=250)
  story = models.TextField()
# Create your models here.
