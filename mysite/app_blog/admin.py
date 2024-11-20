from django.contrib import admin
from .models import Article, ArticleImage, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)


admin.site.register(Article, ArticleAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0


admin.site.register(ArticleImage)
