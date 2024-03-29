from django.contrib import admin
from blog.models import Profile, Post, Comments

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comments)