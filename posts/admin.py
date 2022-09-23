from django.contrib import admin

from posts.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_at")
    list_filter = ("created_at",)
    fields = ("author", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("author",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("title",)
