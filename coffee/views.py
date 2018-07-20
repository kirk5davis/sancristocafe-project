from django.shortcuts import render

from .models import Coffee

# Create your views here.
def home(request):
	coffees = Coffee.objects.all()
	print(coffees)
	return render(request, 'coffee/home.html', {"coffees":coffees})