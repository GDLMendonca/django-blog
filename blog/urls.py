#Handle blog URLs
from django.urls import path
from . import views

urlpatterns = [
	#Handle blog default route
    path('', views.home, name='blog-home'),#Named 'blog-home' instead of 'home' to avoid conflicting variables
	#Handle about cogini.co page
	path('about/', views.about, name='blog-about'),
]