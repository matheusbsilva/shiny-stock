from django.db import models

class ItemType(models.Model):
    description_item = models.CharField(max_length=50,blank=False,null=False)


class UnityType(models.Model):
    description_unity = models.CharField(max_length=50,blank=False,null=False)
    size_unity = models.CharField(max_length=10,blank=True,null=True)


class Item(models.Model):
    name_item = models.CharField(max_length=50,blank=False,null=False)
    quantity_item = models.IntegerField(blank=False,null=False,default=0)
    item_type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    unity_type = models.ForeignKey(UnityType,on_delete=models.CASCADE)


""" Operation types are in portuguese-BR """
OPERATION_TYPES = (
    ('0','Item retirado'),
    ('1','Item inserido'),
)


class History(models.Model):
    date = models.DateField(auto_now=True,blank=False,null=False)
    operation_type = models.CharField(
            max_length=1,
            choices=OPERATION_TYPES,
            blank=False,
            null=False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
