from django.views import generic
from django.urls import reverse_lazy

from .models import Item, ItemType, UnityType
from .forms import ItemForm, ItemTypeForm, UnityTypeForm

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
    template_name = 'items/new.html'
    success_url = reverse_lazy('items:items_index')
    form_class = ItemForm


class ItemUpdate(generic.UpdateView):
    model = Item
    template_name = 'items/edit.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy('items:items_detail', kwargs={'pk':self.kwargs['pk']})


class ItemDelete(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('items:items_index')


class ItemTypeIndex(generic.ListView):
    model = ItemType
    template_name='itemtype/index.html'
    context_object_name = 'itemtype_list'

    def get_queryset(self):
        return ItemType.objects.all()


class ItemTypeDetail(generic.DetailView):
    model = ItemType
    template_name = 'itemtype/detail.html'


class ItemTypeCreate(generic.CreateView):
    model = ItemType
    template_name = 'itemtype/new.html'
    success_url = reverse_lazy('items:itemtype_index')
    form_class = ItemTypeForm


class ItemTypeUpdate(generic.UpdateView):
    model = ItemType
    template_name = 'itemtype/edit.html'
    form_class = ItemTypeForm

    def get_success_url(self):
        return reverse_lazy('items:itemtype_index')


class ItemTypeDelete(generic.DeleteView):
    model = ItemType
    success_url = reverse_lazy('items:itemtype_index')


class UnityTypeIndex(generic.ListView):
    model = UnityType
    template_name = 'unitytype/index.html'
    context_object_name = 'unitytype_list'

    def get_queryset(self):
        return UnityType.objects.all()


class UnityTypeDetail(generic.DetailView):
    model = UnityType
    template_name = 'unitytype/detail.html'


class UnityTypeCreate(generic.CreateView):
    model = UnityType
    template_name = 'unitytype/new.html'
    success_url = reverse_lazy('items:unitytype_index')
    form_class = UnityTypeForm 
