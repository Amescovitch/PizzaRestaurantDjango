from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(
         attrs={
            'placeholder':'Nom et prénom(s):',
            'class': 'name'
        }
    ))
    email = forms.EmailField(label='',required=False, widget=forms.EmailInput(
        attrs={
            'placeholder':'Adresse email (optionnel):',
            'class':'email',
        }
    ))
    telephone = forms.IntegerField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder':'Numéro de téléphone:',
            'class': 'telephone'
        }
    ))
    description_commande = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder':'Décrivez votre commande: nom de la (des) pizzas, nombre.',
            'class': 'description',
        }
    ))
  

