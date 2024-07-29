

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# Create your views here.

def register(request):
    if request.method == 'POST':
       
      username= request.POST.get('username')
      lname= request.POST.get('lname')
      fname= request.POST.get('fname')
      email= request.POST.get('email')
      pass1= request.POST.get('pass1')
      pass2= request.POST.get('pass2')
      
      # to chack if user already exist
      
          
        
      if User.objects.filter(email=email).exists():
          messages.error(request, 'Email address already taken')
         
          return redirect('register')
      
     
      if User.objects.filter(username=username).exists():
          messages.error(request, 'Username already taken')
         
          return redirect('register')
      
      if pass1 != pass2:
          messages.error(request, 'Password does not match')
          print('pass')
          return redirect('register')
      
      # register user to db below
      
      myuser = User.objects.create_user(username,email,pass1)
      myuser.first_name=fname
      myuser.last_name=lname
      
      myuser.save()
      
   
      
      # message handler below
      
      messages.success(request,'accoun has been created')
      
      return redirect('login')
    return render(request,'registration.html')
    
    
def login_user(request):
      if request.method=='POST':
        username= request.POST.get('username')
        pass1= request.POST.get('pass1')
    
   #  auth user
   
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request,'index.html', {'fname':fname})
        else:
            messages.error(request,"bad credential")
            return redirect('login')
      return render(request,'login.html')
   
def logout_user(request):
    logout(request)
    messages.success(request, '  Logged out succesfully')
    return redirect('login')