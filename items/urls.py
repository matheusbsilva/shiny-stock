from django.urls import path

from . import views

app_name = 'items'
urlpatterns = [

    path('', views.ItemIndex.as_view(), name='items_index'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
    path('new',views.ItemCreate.as_view(),name='items_new'),
    path('<int:pk>/edit', views.ItemUpdate.as_view(), name='items_edit'),
    path('<int:pk>/delete', views.ItemDelete.as_view(), name='items_delete'),

    path('type/', views.ItemTypeIndex.as_view(), name='itemtype_index'),
    path('type/<int:pk>/', views.ItemTypeDetail.as_view(), name='itemtype_detail'),
    path('type/new', views.ItemTypeCreate.as_view(), name='itemtype_new'),
    path('type/<int:pk>/edit', views.ItemTypeUpdate.as_view(), name='itemtype_edit'),
    path('type/<int:pk>/delete', views.ItemTypeDelete.as_view(), name='itemtype_delete'),

    path('unity/', views.UnityTypeIndex.as_view(), name='unitytype_index'),
    path('unity/<int:pk>/', views.UnityTypeDetail.as_view(), name='unitytype_detail'),
]
