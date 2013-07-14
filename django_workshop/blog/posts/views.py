from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	return render(request, "posts/post_list.html", {
		'post_list': Post.objects.all()
		})
	# this dict is the "context" - the custom variables that you won't have in template already

def post_detail(request, slug):
	# pk is primary key - the identifier of one single post. the pk is the auto-incrementing ID in the db. 
	post = get_object_or_404(Post, slug=slug)
	return render(request, "posts/post_detail.html", {
		'post': post
		})
