from django.db import models


class Post(models.Model):
    author = models.TextField()
    title = models.TextField()
    content = models.TextField()


class PostView(models.Model):
    forWhatPost = models.IntegerField()
