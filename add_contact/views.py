from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'add_contact/index.html', {'contacts': contacts, 'search_input': search_input})

def addContact(request):
    if request.method == 'POST':

        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address'],
            )
        new_contact.save()
        return redirect('/contacts')

    return render(request, 'add_contact/new.html')

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/contacts/profile/'+str(contact.id))
    return render(request, 'add_contact/edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/contacts')

    return render(request, 'add_contact/delete.html', {'contact': contact})

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'add_contact/contact-profile.html', {'contact':contact})