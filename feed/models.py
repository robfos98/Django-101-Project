from tkinter import CASCADE
from django.db import models
from sorl.thumbnail import ImageField

class Comment(models.Model):
    text = models.CharField(max_length=1023, blank=False, null=False)
    post = models.ForeignKey('feed.Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

class Post(models.Model):
    text = models.CharField(max_length=255, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.text