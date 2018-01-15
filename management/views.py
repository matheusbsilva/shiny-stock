from django.views import generic
from django.urls import reverse_lazy

from .models import Operation
from .forms import OperationForm

class OperationCreate(generic.CreateView):
    model = Operation 
    template_name = 'operation/new.html'
    form_class = OperationForm

    def get_sucess_url(self):
        return reverse_lazy('items:items_detail', kwargs={'pk':self.kwargs['item__id']})
