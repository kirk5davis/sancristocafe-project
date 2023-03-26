from django.shortcuts import render

from .models import Coffee, OfferingsList
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
	current_offering_list = OfferingsList.objects.all().order_by('-date_current')[0]
	return render(request, 'coffee/our_coffees.html', {"coffees":coffees_grouped_twos, "offering_list": current_offering_list})

def source_work(request):
	latest_newsletter = Newsletter.objects.all().order_by('-vintage')[0]
	return render(request, 'coffee/source_work.html', {"newsletter":latest_newsletter})

def source_ethiopia(request):
	return render(request, 'coffee/source_ethiopia.html')

def source_mexico(request):
	return render(request, 'coffee/source_mexico.html')

def traceability(request):
	return render(request, 'coffee/traceability.html')