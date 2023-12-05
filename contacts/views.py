from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    num_mem = contacts.count()
    
    return render(request, 'index.html', {'contacts': contacts, 'num_mem': num_mem})

def addContact(request):
    if request.method == 'POST':

        new_contact = Contact(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            role = request.POST['role-choice']
            )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.first_name = request.POST['firstname']
        contact.last_name = request.POST['lastname']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.role = request.POST['role-choice']
        contact.save()
        
        return redirect('/')
    
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('/')