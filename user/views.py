from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    if request.method=='POST':
        Username=request.POST.get("username")
        Email=request.POST.get("email") 
        Password1=request.POST.get("password1") 
        Password2=request.POST.get(" password2")
        my_user=User.objects.create_user(username=Username,password=Password1)
        my_user.save()
        return redirect('login')
    return render(request,'user/signup.html')

def login_user(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        Password1=request.POST.get('password1')
        user=authenticate(request,username=Username,password=Password1)
        print(user)
        if user is not None:
            request.session['username']=Username
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("INVALID USERNAME AND PASSWORD")
    return render(request,'user/login.html')
        
def logout_user(request):
    logout(request)
    return redirect('login')

