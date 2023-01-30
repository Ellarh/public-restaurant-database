from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    website = models.URLField()
    phone_number = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(default=now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all:detail', kwargs={'pk': self.pk})
