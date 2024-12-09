from django.shortcuts import render,redirect
from apple.models import Item
from django.contrib.auth.models import User
from .models import Cart
# Create your views here.

def cart(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        print(pid)
        print(request.session.get('username'))
        username = User.objects.get(username = request.session.get('username'))
        print(username)
        name = Item.objects.get(id = pid)
        print(name)
        product = Item.objects.filter(id = pid)
        print(product)
        productc = Cart.objects.filter(name = name,username__username = username)
        print(productc)
        if productc:
            for i in productc:
                quantity = i.quantity + 1
                total_price = i.price * quantity
            Cart.objects.filter(name = name,username__username=username).update(quantity = quantity,total_price = total_price)
        else:
            for p in product:
                price = p.item_price
                desc = p.item_desc
                image = p.item_image
            mycart = Cart.objects.create(username = username,name = name,price = price,desc = desc,image = image,total_price = price,quantity = 1)
            mycart.save()
    return redirect('home')


def showcart(request):
    username = request.session.get('username')
    print(username)
    context = {}
    products = Cart.objects.filter(username__username = username)
    print(products)
    context['products'] = products
    return render(request,'cart/cart.html',context)

def deletefromcart(request):
    # username=request.session.get('username')
    if request.method=="POST":
        cid=request.POST.get('cid')
        print(cid)
        # item=Item.objects.get(item_name=Pname)
        # print(item)
        items=Cart.objects.get(id = cid)
        print("Deleted")
        items.delete()
    # context={}
    # itemss=Cart.objects.filter(username__username=username)
    # context['items']=items
    return redirect('showcart')
    

