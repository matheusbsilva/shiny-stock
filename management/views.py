from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect

from items.models import Item
from .models import Operation, Profile
from .forms import OperationForm, SignUpForm

class OperationCreate(generic.CreateView):
    model = Operation 
    template_name = 'operation/new.html'
    form_class = OperationForm

    def form_valid(self,form):
        form.instance.item = Item.objects.get(pk=self.kwargs['item_id'])
        return super().form_valid(form)

    def get_sucess_url(self):
        return reverse_lazy('items:items_detail', kwargs={'pk':self.kwargs['item_id']})


class UserCreate(generic.CreateView):
    template_name = 'profile/new.html'
    form_class = SignUpForm
    success_url = reverse_lazy('items:items_index')

    def form_valid(self, form):
        user = form.save()
        user.profile = Profile.objects.create(address = form.cleaned_data['address'],
                phone = form.cleaned_data['phone'], user = user)

        user.save()

        return redirect(reverse_lazy('items:items_index')) 
