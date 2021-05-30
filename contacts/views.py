from django.shortcuts import redirect, render
from django.contrib import messages
from . models import contact_form
from django.contrib.auth.models import User

# Create your views here
def contactus(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        # user_obj = User.objects.get(id=user_id)
        
        user_name = request.POST['name']
        user_contactno = request.POST['contactno']
        user_emailid = request.POST['emailid']
        companyname = request.POST['companyname']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = contact_form(user_id=user_id, name=user_name, contactno=user_contactno, emailid=user_emailid, companyname=companyname, subject=subject, message=message)
        contact.save()
        messages.success(request, "Thank you for reaching out to us. We will contact you soon.")
        return redirect('home')