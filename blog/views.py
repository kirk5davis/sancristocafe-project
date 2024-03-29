from django.shortcuts import render, get_object_or_404
import os

from .models import Blog
from .models import ArchivedFile
from .models import Newsletter

# Create your views here.
def news(request):
	blog = Blog.objects.all().order_by('-created_on')[0]
	latest_newsletter = Newsletter.objects.all().order_by('-vintage')[0]
	return render(request, 'blog/news.html', {"blog":blog, "newsletter":latest_newsletter})

def blog(request):
	blogs = Blog.objects.all().order_by('-created_on')
	return render(request, 'blog/blog.html', {"blogs":blogs})

def newsletter(request):
	latest_newsletter = Newsletter.objects.all().order_by('-vintage')[0]
	return render(request, 'blog/newsletter.html', {"newsletter":latest_newsletter})

def post_details(request, blog_id):
	post_detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/post_detail.html', {"post_detail":post_detail})

def archives(request):
	archives = ArchivedFile.objects.all().order_by('-vintage')
	older_newsletters = Newsletter.objects.all().order_by('-vintage')[1:]
	return render(request, 'blog/archives.html', {"archived_files":archives, "newsletters":older_newsletters})

def archive_details(request, archive_id, type):
	if type == "newsletter":
		archive_detail = get_object_or_404(Newsletter, pk=archive_id)
	if type == "document":
		archive_detail = get_object_or_404(ArchivedFile, pk=archive_id)
	return render(request, 'blog/archives_doc_view.html', {"archive_file":archive_detail})