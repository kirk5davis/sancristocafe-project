from django.shortcuts import render

from .models import Coffee
from blog.models import Blog
from blog.models import Newsletter

# Create your views here.
def home(request):
	just_three_blogs = Blog.objects.all().order_by('-created_on')[0:3]
	return render(request, 'coffee/home.html', {"blogs":just_three_blogs})

def about(request):
	return render(request, 'coffee/about.html')

def coffees(request):
	coffees = Coffee.objects.all()
	coffees_grouped_twos = [coffees[i * 2:(i + 1) * 2] for i in range((len(coffees) + 2 - 1) // 2 )]
	return render(request, 'coffee/our_coffees.html', {"coffees":coffees_grouped_twos})

def source_work(request):
	latest_newsletter = Newsletter.objects.all().order_by('-vintage')[0]
	return render(request, 'coffee/source_work.html', {"newsletter":latest_newsletter})

def traceability(request):
	return render(request, 'coffee/traceability.html')