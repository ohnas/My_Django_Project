from django.db import models
from core.models import TimeStampeModel
from users.models import User


# Create your models here.


class Product(TimeStampeModel):

    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
