from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

# def contact(request):
#     if request.method == 'POST':
       
#       name= request.POST.get('Name')
#       phone= request.POST.get('Phone')
#       email= request.POST.get('Email')
#       message= request.POST.get('Message')
      
      #send email
      
    #   send_mail( 
    #     name,
    #     phone,
    #     email,
    #     message,
    #   ['jichangwookjcw69@gmail.com']
      
    #   ) 
    



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        
        # Compose the email message
        email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        if phone:
            email_message += f"\nPhone: {phone}"
        
        # Send email
        send_mail(
            'Contact Form Submission',  # Subject
            email_message,  # Message
            email,  # Sender's email address (assuming the form provides it)
            ['jichangwookjcw69@gmail.com'],  # List of recipient(s) as a single-element list
            fail_silently=False,  # Set to True to suppress exceptions
        )

    return render(request, 'contact.html')

    
    
    
    
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def shop(request):
    return render(request,'shop.html')

def about(request):
    return render(request,'about.html')
