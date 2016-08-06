from django.db import models


def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.title, filename)

class Trailer(models.Model):
    title = models.CharField(max_length=500)
    embed_link = models.TextField()
    approved = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    release = models.IntegerField(default=2000)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

