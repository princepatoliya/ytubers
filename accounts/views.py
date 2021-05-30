from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages, auth


from django.contrib.auth.models import User
from .models import *
from hiretubers.models import HireTuber

import uuid

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            profile_obj = Profile.objects.filter(user = user).first()
            if profile_obj.is_verified:
                auth.login(request, user)
                messages.success(request, f"Welcome {username}, you are logged in")
                return redirect('dashboard')
            else:
                messages.info(request, "Your account is not verified, Please check you mail")
                return redirect('login')
        else:
            messages.warning(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request): 

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request, "Username exists.")
                return redirect('register')
            else:
                if User.objects.filter(email = email).first():
                    messages.warning(request, "Email is already exists")
                    return redirect('register')
                else:
                    try:
                        auth_token=str(uuid.uuid4())
                       
                        # send email for verification, if email send then and then create account
                        if send_mail_after_register(email, auth_token):
                            # save user details
                            user_obj = User(first_name = firstname, last_name=lastname, username=username, email=email)
                            user_obj.set_password(password)
                            user_obj.save()

                            # save user from user_obj and token generate via uuid
                            profile_obj = Profile(user = user_obj, auth_token = auth_token)
                            profile_obj.save()
                            
                            messages.success(request, "Account created successfully, Please check your email for verification.")
                            return redirect('login')

                    except Exception as error:
                        print("While saving user details or sending email" ,error)
        else:
            messages.warning(request, "Password does not match")
            return redirect('register')

        
    
    return render(request, 'accounts/register.html')


def send_mail_after_register(reciver_email, token):
    try:
        email = EmailMessage(
            'Your new "YTubers-Account" needs to be verified',
            f'This message from YTubers, Please click on this link to verify your account http://127.0.0.1:8000/accounts/verify/{token} ',
            settings.EMAIL_HOST_USER,
            [reciver_email],
        )
        email.fail_silently = False
        email.send()
        return True

    except Exception as error:
        print("While sending email: ", error)
        return False


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        
        if profile_obj:
            if profile_obj.is_verified:
                messages.info(request, "Your account is already verified.")
                return redirect('login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "Your Account has been verified.")
            return redirect('login')
        else:
            messages.warning(request, "Invalid token detected.")
    
    except Exception as error:
        messages.warning(request, "Invalid token detected.")
        print(error)
        return redirect('login')



@login_required(login_url='login')  
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')    
def dashboard(request):

    ytuber = HireTuber.objects.filter(user_id = request.user.id)

    data = {
        'ytuber': ytuber,
    }

    return render(request, 'accounts/dashboard.html', data)


