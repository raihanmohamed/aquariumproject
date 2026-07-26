from django.db import models


class Fish(models.Model):
    fish_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    tank_number = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.fish_name
