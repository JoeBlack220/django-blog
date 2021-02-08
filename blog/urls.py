from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('tags', views.tags, name='tags'),
]
