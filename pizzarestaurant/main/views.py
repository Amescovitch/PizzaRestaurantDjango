from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# /main
def index(request):
    return render(request, 'main/index.html')
