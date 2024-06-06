from django.contrib import admin
from posts.models import Post, Category, ProducerPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'en_title', 'pr_title', 'create_at', 'update_at', 'is_published']
    list_filter = ['is_published', 'create_at', 'update_at']
    raw_id_fields = ['author', 'tag']
    search_fields = ['title', 'body']
    prepopulated_fields = {'en_slug': ('en_title',), 'fa_slug': ('pr_title',)}
    date_hierarchy = 'create_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'en_category_title', 'en_category_title', 'en_category_slug', 'pr_category_slug']
    list_filter = ['create_at', 'is_published']
    search_fields = ['category_title']
    prepopulated_fields = {'en_category_slug': ('en_category_title',), 'pr_category_slug': ('pr_category_title',)}


@admin.register(ProducerPost)
class ProducerPostAdmin(admin.ModelAdmin):
    list_display = ['producer_name', 'producer_is_active']
    list_filter = ['producer_is_active', 'create_at', 'update_at']
    search_fields = ['producer_name']
    