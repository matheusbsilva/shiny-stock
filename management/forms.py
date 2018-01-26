from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['amount','operation_type']


class SignUpForm(UserCreationForm):
    address = forms.CharField()
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username','password1','password2','address','phone')
