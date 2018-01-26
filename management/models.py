from django.db import models
from django.contrib.auth.models import User

from items.models import Item

""" Operation types are in portuguese-BR """
""" 0 for items removed """
""" 1 for items added """
OPERATION_TYPES = (
    ('0','Item retirado'),
    ('1','Item inserido'),
)


class Operation(models.Model):
    date = models.DateField(auto_now=True,blank=False,null=False)
    amount = models.IntegerField(blank=False, null=False)
    operation_type = models.CharField(
            max_length=1,
            choices=OPERATION_TYPES,
            blank=False,
            null=False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.date) + '-' + self.item.name_item)


class Profile(models.Model) :
    # Using django auth User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=50)
    phone = models.IntegerField(blank=True, null=True, max_length=15)
