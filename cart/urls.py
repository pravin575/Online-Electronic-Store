from django.urls import path
from .import views

urlpatterns = [
    path('cart',views.cart),
    path('show',views.showcart,name='showcart'),
    path('delete',views.deletefromcart),
]