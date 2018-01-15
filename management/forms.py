from django.forms import ModelForm

from .models import Operation

class OperationForm(ModelForm):
    # operation_type = operation
    # item = item_updated
    class Meta:
        model = Operation 
        fields = ['amount','operation_type','item']

