from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse

from .models import Item
from .forms import ItemForm

class IndexView(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()


class DetailView(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'

def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            name_item = form.cleaned_data['name_item']
            quantity_item = form.cleaned_data['quantity_item']
            item_type = form.cleaned_data['item_type']
            unity_type = form.cleaned_data['unity_type']

            item = Item.objects.create(name_item=name_item,
                    quantity_item=quantity_item,item_type=item_type,unity_type=unity_type)

            return HttpResponseRedirect(reverse('items:index'))
    else:
        form = ItemForm()

    return render(request,'items/new_item.html', {'form':form})
