from django.db import models
from django.urls import reverse
# Create your models here.


class Toy(models.Model):
    name = models.CharField(max_length=200)
    start_age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy_edit', kwargs={'pk': self.pk})