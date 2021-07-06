from django.contrib import messages
from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact.objects.create(name = name, email = email, phone_number = phone, message = message)
        contact.save()
        messages.success(request, 'your message has been sent successfully !!')

    return render(request, 'contact/contact.html')
   
