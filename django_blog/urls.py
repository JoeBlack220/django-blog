"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('archives/', views.Archives.as_view(), name='archive'),
    path('tags/', views.Tags.as_view(), name='tags'),
    path('tags/<str:tag>', views.TagsDetail.as_view(),
         name='atgs_detail'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('categories/<str:cate>', views.CategoriesDetail.as_view(),
         name='categories_detail'),
    path('posts/<slug:the_slug>/', views.Detail.as_view(), name='show_post'),
]
