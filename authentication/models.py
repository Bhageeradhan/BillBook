from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     age = models.IntegerField(default=0)
     
     ADMIN = 0
     MANAGER = 1
     EMPLOYEE = 2
     
     role_choices = (
          (ADMIN,'admin'),
          (MANAGER,'manager'),
          (EMPLOYEE,'employee'),
     )
     
     role = models.IntegerField(default=0, choices= role_choices)
