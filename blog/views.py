import random
import datetime
import markdown2
from operator import itemgetter
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .utils import convert_toc

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

        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'all_articles': articles,
        })


class Detail(View):
    """
    Detail page
    """

    def get(self, request, the_slug):
        article = Article.objects.get(slug=the_slug)
        all_articles = Article.objects.all().order_by('-add_time')
        prev_a, cur_a, next_a = None, None, None

        for i in range(len(all_articles)):
            if all_articles[i].slug == the_slug:
                if i != 0:
                    prev_a = all_articles[i-1]
                if i != len(all_articles) - 1:
                    next_a = all_articles[i+1]

        article.viewed()
        md = markdown2.Markdown(extras=["toc", "header-ids"])
        content = md.convert(article.content)
        print(convert_toc(content.toc_html))
        return render(request, 'detail.html', {
            'article': article,
            'content': content,
            'toc': convert_toc(content.toc_html),
            'prev': prev_a,
            'next': next_a,
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
