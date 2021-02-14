import random
import datetime
import markdown
from operator import itemgetter
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .utils import convert_toc
from .models import Article, Category, Tag, About

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

        md = markdown.Markdown(
            extensions=['toc', 'extra', 'codehilite', 'header-ids'])
        content = md.convert(article.content)

        return render(request, 'detail.html', {
            'article': article,
            'content': content,
            'toc': convert_toc(md.toc),
            'prev': prev_a,
            'next': next_a,
        })


class Tags(View):
    """
    Categories page
    """

    def get(self, request):
        all_tags = Tag.objects.all()

        return render(request, 'tags.html', {
            'tags': all_tags,
        })


class AboutPage(View):
    """
    About page
    """

    def get(self, request):
        about = About.objects.all()[0]

        md = markdown.Markdown(
            extensions=['toc', 'extra', 'codehilite', 'header-ids'])
        content = md.convert(about.content)
        return render(request, 'about.html', {
            'content': content
        })


class Categories(View):
    """
    Categories page
    """

    def get(self, request):
        all_categories = Category.objects.all()

        return render(request, 'categories.html', {
            'categories': all_categories,
        })


class TagsDetail(View):
    """
    Tag articles page
    """

    def get(self, request, tag):
        category = Tag.objects.get(name=tag)
        all_articles = category.article_set.all()

        # Pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'all_articles': articles,
        })


class CategoriesDetail(View):
    """
    Categories page
    """

    def get(self, request, cate):
        category = Category.objects.get(name=cate)
        all_articles = category.article_set.all()

        # Pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'all_articles': articles,
        })


class Archives(View):
    """
    Archive page
    """

    def get(self, request):
        all_articles = Article.objects.all().order_by('-add_time')
        # Archives paginatio
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 15, request=request)
        articles = p.page(page)
        print(articles)
        return render(request, 'archives.html', {
            'all_articles': articles,
            'num': len(all_articles),
        })
