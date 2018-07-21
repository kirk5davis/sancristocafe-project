from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def blogs(request):
	blogs = Blog.objects.all().order_by('-created_on')
	return render(request, 'blog/blogs.html', {"blogs":blogs})

def post_details(request, blog_id):
	post_detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/post_detail.html', {"post_detail":post_detail})