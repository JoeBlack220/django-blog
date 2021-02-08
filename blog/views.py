import random
import datetime
import mistune
from operator import itemgetter
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Category, Tag

# Create your views here.


class Index(View):
    """
    Index page
    """

    def get(self, request):
        all_articles = Article.objects.all().order_by('-add_time')
        # 首页分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 9, request=request)
        articles = p.page(page)

        return render(request, 'index.html', {
            'all_articles': articles,
        })


def blog(request):
    return render(request, 'index.html')


def tags(request):
    return render(request, 'tags.html')


def about(request):
    return render(request, 'about.html')


def categories(request):
    return render(request, 'categories.html')


def archives(request):
    return render(request, 'archives.html')
