from django.db import models
from datetime import datetime
from django.utils.html import format_html
from mdeditor.fields import MDTextField

# Create your models here.


class Tag(models.Model):
    """
    Tags for articles
    """
    name = models.CharField(max_length=30, verbose_name='tag name')

    # Count the number of articles
    def get_num(self):
        return len(self.article_set.all())

    get_num.short_description = 'number of articiles'

    class Meta:
        verbose_name = 'tag name'
        verbose_name_plural = 'tag names'

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Categories for articles
    """
    name = models.CharField(max_length=30, verbose_name='category names')
    index = models.IntegerField(default=99, verbose_name='category index')
    icon = models.CharField(
        max_length=30, default='fa-home', verbose_name='icon')

    # Count the number of articles
    def get_num(self):
        return len(self.article_set.all())

    def icon_data(self):
        return format_html(
            '<i class="{}"></i>',
            self.icon,
        )

    get_num.short_description = 'number of articles'
    icon_data.short_description = 'preview of cons'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Articles
    """
    title = models.CharField(max_length=50, verbose_name='article Title')
    desc = models.TextField(max_length=100, verbose_name='article Description')
    content = MDTextField(verbose_name='article content')
    click_count = models.IntegerField(default=0, verbose_name='click count')
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name='post time')
    update_time = models.DateTimeField(
        auto_now=True, verbose_name='update time')
    category = models.ForeignKey(
        Category, blank=True, null=True, verbose_name='category names', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    tag = models.ManyToManyField(Tag, verbose_name='tag names')

    def viewed(self):
        """
        Increase viewed count
        """
        self.click_count += 1
        self.save(update_fields=['click_count'])

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


class About(models.Model):
    """
    About
    """
    content = MDTextField(verbose_name='article content')
