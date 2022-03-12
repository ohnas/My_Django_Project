from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    company_code = models.IntegerField(blank=True, null=True)
