from django.urls import path

from . import views

app_name = 'management'

urlpatterns = [
        path('operation/<int:item_id>/new', views.OperationCreate.as_view(), name='operation_new'),

]
