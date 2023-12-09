from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
class Index(ListView):
    model = Contact
    template_name = "index.html"
    context_object_name = "contact_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_mem"] = context['contact_list'].count()
        return context
    
class Add(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'new.html'
    success_url = "/"
    
class Edit(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'edit.html'
    success_url = "/"
    

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('/')