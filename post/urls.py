from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.listAllProduct, name='post'),
    path('listAllProduct', views.listAllProduct, name='listAllproduct'),
    path('uploadProduct', views.uploadProduct, name='uploadProduct'),
    path('myProduct', views.myProduct, name='listMyProduct'),
    path('myCart', views.listAllMyCart, name='listMyCart'),
    path('purchaseHistory', views.displayHistory, name='listOrderHistory'),

]
