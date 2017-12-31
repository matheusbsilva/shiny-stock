from django.db import models

class ItemType(models.Model):
    description_item = models.CharField(max_length=50,blank=False,null=False)


class UnityType(models.Model):
    description_unity = models.CharField(max_length=50,blank=False,null=False)


class Item(models.Model):
    name_item = models.CharField(max_length=50,blank=False,null=False)
    quantity_item = models.IntegerField(blank=False,null=False,default=0)
    item_type = models.ForeignKey(ItemType)
    unity_type = models.ForeignKey(UnityType)


OPERATION_TYPES = (
    """ Operation types are in portuguese-BR """
    ('0','Item inserido'),
    ('1','Item retirado'),
)


class History(models.Model):
    date = DateField(blank=False,null=False)
    operation_type = models.CharField(
            max_length=1,
            choices=OPERATION_TYPES,
            blank=False,
            null=False)
    item = models.ForeignKey(Item)
