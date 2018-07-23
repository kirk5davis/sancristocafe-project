from django.shortcuts import render

from .models import Coffee
from blog.models import Blog

# Create your views here.
def home(request):
	just_three_blogs = Blog.objects.all().order_by('-created_on')[0:3]
	coffees = Coffee.objects
	return render(request, 'coffee/home.html', {"coffees":coffees, "blogs":just_three_blogs})

def about(request):
	return render(request, 'coffee/about.html')

def coffees(request):
	coffees = Coffee.objects
	return render(request, 'coffee/our_coffees.html',{"coffees":coffees})

def source_work(request):
	return render(request, 'coffee/source_work.html')