from django.views import generic
from django.urls import reverse_lazy

from .models import Item
from .forms import ItemForm

class ItemIndex(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()


class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'


class ItemCreate(generic.CreateView):
    model = Item
    template_name = 'items/new_item.html'
    success_url = reverse_lazy('items:index')
    form_class = ItemForm


class ItemUpdate(generic.UpdateView):
    model = Item
    template_name = 'items/edit_item.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy('items:detail', kwargs={'pk':self.kwargs['pk']})


class ItemDelete(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('items:index')
