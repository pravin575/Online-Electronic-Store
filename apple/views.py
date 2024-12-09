from django.shortcuts import render
from  .models import Item 
from .models import Item
# Create your views here.

def apple(request):
    context={}
    applee=Item.objects.all()
    print(applee)
    context['apple']=applee
    return render(request,'apple/apple.html',context)

def search(request):
    context={}
    if request.method=='POST':
        Productname=request.POST['productname']
        print(Productname)
        product=Item.objects.filter(item_name__contains=Productname)
        context['product']=product
    return render(request,'apple/search.html',context)