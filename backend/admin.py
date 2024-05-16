from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


@admin.register(News)
class PostsAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'photo')
    list_display = ('id', 'title', 'photo', 'post_photo', 'time_created')
    list_display_links = ('id', 'title')
    ordering = ['-time_created', 'title']
    search_fields = ['title']
    readonly_fields = ['post_photo']
    save_on_top = True

    @admin.display(description='Фото')
    def post_photo(self, request):
        if request.photo:
            return mark_safe(f'<img src={request.photo.url} width=100>')
        return 'Без фото'
