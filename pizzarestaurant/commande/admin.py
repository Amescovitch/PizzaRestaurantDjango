from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone', 'description_commande')
    search_fields = ['description_commande']

# Register your models here.


admin.site.register(Contact, ContactAdmin)

