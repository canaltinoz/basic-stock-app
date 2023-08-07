from django.db import models
from django.contrib.auth.models import User
from app.models import Flavour
from django.db.models import Sum

# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import BaseUserManager
# from django.conf import settings

class UserBalance(models.Model):
    starting_amount = models.PositiveIntegerField(default=100000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_current_balance(self,starting_amount):
        total_expenses = sum(q.total for q in Flavour.objects.all())
        return self.starting_amount-total_expenses
       
    
    # def change_amount(self,starting_amount):
    #     for _ in Flavour.objects.get():
    #         sum+=Flavour.objects.get().total
    #     amount-=sum
    #     return amount

# class UserProfileManager(BaseUserManager):
#     """manager for user profiles"""

#     def create_user(self,email,name,password=None):
#         """create new user profile"""
#         if not email:
#             raise ValueError('User must have an email address')
        
#         email=self.normalize_email(email)
#         user=self.model(email=email,name=name)

#         user.set_password(password)
#         user.save(using=self._db)

#         return user
    
#     def create_superuser(self,email,name,password):

#         user=self.create_user(email,name,password)

#         user.is_superuser= True
#         user.is_staff=True
#         user.save(using=self._db)

#         return user

# class UserProfile(AbstractBaseUser):
#     """database model for users in the system"""

#     email=models.EmailField(max_length=255,unique=True)
#     name=models.CharField(max_length=255)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)

#     objects=UserProfileManager()

#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS=['name']

#     def get_full_name(self):
#         """retrieve full name of user"""
#         return self.name

#     def get_short_name(self):
#         """retrieve short name of user"""
#         return self.name
    
#     def __str__(self):
#         """return string representation of our user"""
#         return self.email
