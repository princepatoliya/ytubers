from django.shortcuts import redirect, render
from .models import HireTuber
from youtubers.models import Youtuber

from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings # for retrive our data that we config in settings.py file [170-175 lines]
from django.template.loader import render_to_string # grab the tempalates and allow to send as a sting in email



def hiretuber(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email_id']

        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tubername']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']

        
        #info for email_template.html
        template_data = {
            'name' : tuber_name,
            'first_name': first_name,
            'last_name': last_name,
            'email_id' : email_id,
            'contact_no' : phone,
            'message' : message,
        }

        template = render_to_string('../templates/email_template.html', template_data)
        # print('template : ', template)
        reciver_tuber_emailid = Youtuber.objects.get(id=tuber_id).emailid
        # print('reciver_tuber_emailid', reciver_tuber_emailid)
        email = EmailMessage(
            'Hiring from YTuber! Customer:' + first_name,
            template,
            settings.EMAIL_HOST_USER,
            [reciver_tuber_emailid],
        )
        email.fail_silently=False
        try:
            email.send()
            hire = HireTuber(user_id=user_id, first_name=first_name, last_name=last_name, email_id=email_id, tuber_id=tuber_id, tuber_name=tuber_name, city=city, state=state, phone=phone, messages=message)
            hire.save()
            messages.success(request, f"Thank you for reaching out to {tuber_name}. They will contact you soon.")
        
        except Exception as error:
            print(error)


        return redirect('youtubers')

