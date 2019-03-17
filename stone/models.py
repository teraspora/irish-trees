from django.db import models

# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length=32, blank=False)
    genus = models.CharField(max_length=32, blank=False)
    species = models.CharField(max_length=32, blank=False)
    origin = models.CharField(max_length=32, blank=False)
    native = models.BooleanField(blank=False, default=True)
    conifer = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name