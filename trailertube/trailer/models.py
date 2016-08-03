from django.db import models

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.title, filename)

class Trailer(models.Model):
    title = models.CharField(max_length=500)
    embed_link = models.TextField()
    like = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    release = models.IntegerField(default=2000)

    def __str__(self):
        return self.title

