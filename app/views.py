from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def home(request):
    
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Username or Password is incorrect")
    

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        html_message = render_to_string('account_mail.html',{"username": username, "email": email})
        plain_message = strip_tags(html_message)
        if cpassword == password:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Account already exist")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Account already exists")
            else:
                 User.objects.create_user(username=username, email=email, password=password, first_name=address)
                 send_email = EmailMultiAlternatives("Giit Mail: Account Creation", plain_message, "info@giitafrica.com", [email] )
                 send_email.attach_alternative(html_message, 'text/html')
                 send_email.send()
                 messages.info(request, "Account Successfully Created")
                


        else:
            messages.info(request, "Password does not match")
    return render(request, 'register.html')

@login_required(login_url='/login/')
def dashboard(request):
    if request.method == "POST":
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        message = request.POST['message']
        html_message = render_to_string('mail_template.html', {'context': 'values', 'message' : message, "recipient" : recipient})
        plain_message = strip_tags(html_message)
        mail = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recipient])
        mail.attach_alternative(html_message, 'text/html')
        mail.send()
        if mail:
            messages.info(request, "Mail Successfully Sent")
        else:
            messages.info(request, "An error ouccured")

    
    return render(request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

def mail(request):
    
    return render(request, 'account_mail.html')

def mailing(request):
    if request.method == "POST":
        recepient = request.POST['recipient']
        subject = request.POST['subject']
        message = request.POST['message']
        select_template = request.POST['template']
        template_file = request.FILES['mailfile']
        imageurl = request.POST['imageurl']
        if select_template == "a":
            html_message = render_to_string('mail_template.html', {"message": message})
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recepient])
            email.attach_alternative(html_message, 'text/html')
            email.attach_file(template_file)
            email.send()
            messages.info(request, "Mail Successfully Sent")
        elif select_template == 'b':
            html_message = render_to_string('mail_template.html', {"message": message})
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recepient])
            email.attach_alternative(html_message, 'text/html')
            email.send()
            messages.info(request, "Mail Successfully Sent")
        elif select_template == 'c':
            html_message = render_to_string('mail_template.html',  {"message": message})
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recepient])
            email.attach_alternative(html_message, 'text/html')
            email.send()
            messages.info(request, "Mail Successfully Sent")
        elif select_template == 'd':
            html_message = render_to_string('mail_template.html',  {"message": message})
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recepient])
            email.attach_alternative(html_message, 'text/html')
            email.send()
            messages.info(request, "Mail Successfully Sent")
        elif select_template == 'e':
            html_message = render_to_string('mail_template.html',  {"message": message})
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, plain_message, settings.EMAIL_HOST_USER, [recepient])
            email.attach_alternative(html_message, 'text/html')
            email.send()
            messages.info(request, "Mail Successfully Sent")
        else:
            messages.info(request, 'Select the correct templates')

    
    return render(request, 'mailing.html')

def profile(request):
    
    return render(request, 'profile.html')

def editprofile(request, id):
    if request.method == "POST":
        address = request.POST['address']
        user = User.objects.get(id=id)
        user.first_name = address
        user.save()
        messages.info(request, "Profile successfully updated")
        

    
    return render(request, 'editprofile.html')