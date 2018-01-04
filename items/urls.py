from django.urls import path 

from . import views

app_name = 'items'
urlpatterns = [
    path('', views.ItemIndex.as_view(), name='index'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='detail'),
    path('new',views.ItemCreate.as_view(),name='new'),
    path('<int:pk>/edit', views.ItemUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', views.ItemDelete.as_view(), name='delete'),
]
