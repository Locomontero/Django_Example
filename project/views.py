from django.shortcuts import render
from project.models import Post

def home(request):
	posts = Post.objects.all()
	return render(request, 'home.html', {'posts': posts})

def post(request, post_id):
	post =Post.objects.get(pk=post_id)
	return render(request, 'post.html', {'post': post})
