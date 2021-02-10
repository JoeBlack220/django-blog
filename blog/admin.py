from django.contrib import admin
from .models import Tag, Category, Article, About
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(About)


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
