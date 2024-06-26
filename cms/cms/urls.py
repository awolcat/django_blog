"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name=''),
    path('signup/', blog_views.signup, name='signup'),  
    path('login/', blog_views.login, name='login'),
    path('logout/', blog_views.logout, name='logout'),
    path('create_post/', blog_views.create_post, name='create_post'),
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),
    path('comment/', blog_views.comments, name='comment'),
    path('tinymce/', include('tinymce.urls')),
]
print(blog_views.comments)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
