from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    topic = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
