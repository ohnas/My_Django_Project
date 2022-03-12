import imp
from django.db import models
from core.models import TimeStampeModel
from products.models import Product
from users.models import User

# Create your models here.


class In(TimeStampeModel):

    name = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
