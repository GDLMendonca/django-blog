#Django database models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Posts table in db
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #Cascade deletes the post if the user is deleted

	#To string method
	def __str__(self):
		return self.title
