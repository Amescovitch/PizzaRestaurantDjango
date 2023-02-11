from django.shortcuts import render
from .models import pizza


# Create your views here.

# / menu
def index(request):
    """pizzas = pizza.objects.all()
    pizzas_names_and_prices = [pizza.nom + ": " + str(pizza.prix) + " FCFA" for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse(f"Les pizzas: {pizzas_names_and_prices_str}")"""
   
    pizzas = pizza.objects.all().order_by("prix")
    return render(request, 'menu/index.html', {'pizzas': pizzas})
