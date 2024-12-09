from django.shortcuts import render,HttpResponse
from cart.models import Cart
from django.contrib.auth.models import User
import string
import random
from checkout.models import Order
from checkout.models import OrderItem
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def checkout(request):
    username=request.session.get('username')
    context={}
    total_amount = 0
    products=Cart.objects.filter(username__username = username)
    for i in products:
        total_amount += i.total_price
    context['products']=products
    context['total_amount'] = total_amount
    print(total_amount)
    return render(request,'checkout/checkout.html',context)

def order(request):
    if request.method=='POST':
        username=User.objects.get(username = request.session.get('username'))
        Mark=request.POST.get('fname')
        Otto=request.POST.get('lname')
        Email=request.POST.get('email')
        address=request.POST.get('city') + request.POST.get('zip')
        full_name = Mark + Otto

        upper = string.ascii_uppercase
        num = string.digits
        all = upper + num
        temp = random.sample(all,10)
        order_id = "ORD" + "" .join(temp)
        print(order_id)
        order_details = Order.objects.create(order_id = order_id,username = username,full_name = full_name,email = Email,shipping_address = address)
        order_details.save()

        paypal_transaction_id = request.POST.get("paypal-button-id")
        print(paypal_transaction_id)
        order_id=Order.objects.get(username__username=username,placed=False)
        cart_items=Cart.objects.filter(username__username=username)
        
        if paypal_transaction_id:
            for cart in cart_items:
                OrderItem.objects.create(
                    order = order_id,
                    product = cart.name,
                    username = username,
                    quantity = cart.quantity,
                    price = cart.price,
                )
                cart.delete()
            Order.objects.filter(username__username=username,placed=False).update(placed = True) 
            return redirect('success')
        
        else:
            return HttpResponse("INVALID PAYMENT INFORMATRION")

def success(request):
    context={}
    username=request.session.get('username')
    order_details=Order.objects.get(username__username = username,emailsend = False)
    subject = 'Order confirmation '+ str(order_details.order_id)
    message='Dear '+ str(order_details.username)+'\n'+'Thank you for your order'
    address=order_details.username.email
    print(address)
    try:
        send_mail(subject,message,settings.EMAIL_HOST_USER, [address])
        context['result'] = 'Email send successfully'
        Order.objects.filter(username__username = username,emailsend = False).update(emailsend = True)
    except Exception as e:
        context['result'] = f'Error sending email:' + e

    return render(request,'checkout/ordertest.html',context)