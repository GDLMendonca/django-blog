from django.shortcuts import render
from .models import Post #Import post DB table model

#Handle homepage of the blog
def home(request):
	#Pass database data into post template
	context = {
		'posts': Post.objects.all()
	}

	#Load HTML view from /templates/blog
	return render(request, 'blog/home.html', context)

#Handle "About Cogini.co" blog page
def about(request):
	return render(request, 'blog/about.html')