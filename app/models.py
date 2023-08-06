from django.db import models

VARIETY_CHOICES = [
    ("Flavour","flavour"),
]

class Flavour(models.Model):
    name=models.CharField(max_length=50)
    variety=models.CharField(max_length=50,choices=VARIETY_CHOICES)
    total=models.PositiveSmallIntegerField(default=0)
