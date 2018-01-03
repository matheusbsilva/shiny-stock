from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Item

class IndexView(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()


class DetailView(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'
