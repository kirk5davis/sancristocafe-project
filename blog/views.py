from django.shortcuts import render

from .models import Blog

# Create your views here.
def blogs(request):
	blogs = Blog.objects.all().order_by('-created_on')
	return render(request, 'blog/blogs.html', {"blogs":blogs})
