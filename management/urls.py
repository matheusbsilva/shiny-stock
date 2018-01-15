from django.urls import path

from . import views

app_name = 'management'

urlpatterns = [
    path('operation/new', views.OperationCreate.as_view(), name='operation_new'),

]
