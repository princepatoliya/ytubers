from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.contrib import messages
from .models import Coffee

import razorpay

from django.conf import settings


# Create your views here.

def donate_page(request):
    if request.method == "POST":
        name = request.POST['name']
        amount = int(request.POST['amount']) * 100

        client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
        # client.set_app_details({"title" : "django", "version" : "3.2.3"})
        notes = {'purpose': 'for testing',}
        payment = client.order.create({'amount' : amount, 'currency' : 'INR' , 'payment_capture' : '1', 'notes': notes})
        print("Payment client.order:-->> ", payment) 

        coffee = Coffee(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()
        data = {
            'payment' : payment,
            }
        return render(request, 'donation/process.html', data)
    
    return render(request, 'donation/donate_page.html')

@csrf_exempt
def success(request):
    if request.method == "POST":
        temp = request.POST
        print(temp)
        order_id = ""
        for key, val in temp.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = Coffee.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        messages.success(request, "Thanks for coffee, Your payment has been recevied.")
        
    
    return render(request, 'donation/donate_page.html')


