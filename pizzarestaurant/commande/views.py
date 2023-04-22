from django.shortcuts import render
from .models import Contact
from .form import ContactForm


def commande(request):
   form = ContactForm()
   message = ''
   if request.method == "POST":
      form = ContactForm(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
         new = Contact.objects.create(**form.cleaned_data)
         new.save()
         form = ContactForm
         message = 'Commande bien envoyée !'

   return render(request, 'commande/index.html', {'form': form, 'message':message})