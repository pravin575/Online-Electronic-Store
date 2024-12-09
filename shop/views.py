from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def home(request):
    context={}
    shope=Product.objects.all()
    # print(shope)
    context['shop']=shope
    return render(request,'shop/home.html',context)
 