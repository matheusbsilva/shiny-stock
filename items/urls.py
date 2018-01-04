from django.urls import path 

from . import views

app_name = 'items'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new',views.new_item,name='new'),
]
