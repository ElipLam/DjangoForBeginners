from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # only show exist comments


class ArticleAdmin(admin.ModelAdmin):  # Custom ArticleAdmin UI
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
