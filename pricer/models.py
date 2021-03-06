from django.db import models
import requests
from bs4 import BeautifulSoup
import pricer.web

BASE_URL = "https://www.poppriceguide.com/guide/searchresults.php?search="


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# TODO update model with data attribute to use for checking if item should be refreshed.
class Pop(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)

    def __str__(self):
        return "{} : {}".format(self.name, self.value)


