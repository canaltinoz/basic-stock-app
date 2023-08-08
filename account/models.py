from django.db import models
from django.contrib.auth.models import User
from app.models import Flavour
from django.contrib import messages


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    starting_amount=models.PositiveBigIntegerField()

    def updating_amount(self):
        flavour=Flavour.objects.all()
        global total_exp
        total_exp = sum(q.total for q in flavour)
        return (self - total_exp)


       
    
