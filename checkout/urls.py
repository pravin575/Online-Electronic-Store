
from django.urls import path
from .import views

urlpatterns = [
   path('',views.order,name='order'),
   path('checkout',views.checkout),
   path('success',views.success,name='success'),
]