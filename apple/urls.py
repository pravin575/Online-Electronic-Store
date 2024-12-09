
from django.urls import path
from .import views

urlpatterns = [
    path('apple',views.apple),
    path('search',views.search),
]