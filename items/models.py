from django.db import models

class ItemType(models.Model):
    description_item = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.description_item


class UnityType(models.Model):
    description_unity = models.CharField(max_length=50,blank=False,null=False)
    size_unity = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.description_unity

class Item(models.Model):
    name_item = models.CharField(max_length=50,blank=False,null=False)
    quantity_item = models.IntegerField(blank=False,null=False,default=0)
    item_type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    unity_type = models.ForeignKey(UnityType,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_item
