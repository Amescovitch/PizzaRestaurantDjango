from django.contrib import admin
from .models import pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredient', 'vegetarienne', 'prix')
    search_fields = ['nom']

# Register your models here.


admin.site.register(pizza, PizzaAdmin)

