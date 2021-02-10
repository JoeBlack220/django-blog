from django.contrib import admin
from .models import Tag, Category, Article
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
# admin.site.register(Article)


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
