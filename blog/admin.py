from django.contrib import admin
from .models import Post

#Get database table models to show on admin page
admin.site.register(Post)
