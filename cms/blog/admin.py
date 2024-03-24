from django.contrib import admin
from blog.models import User, Post, Comments

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comments)