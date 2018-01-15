from django.forms import ModelForm

from .models import Item, ItemType, UnityType

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name_item','quantity_item','item_type','unity_type']


class ItemTypeForm(ModelForm):
    class Meta:
        model = ItemType
        fields = ['description_item']


class UnityTypeForm(ModelForm):
    class Meta:
        model = UnityType
        fields = ['description_unity','size_unity']

