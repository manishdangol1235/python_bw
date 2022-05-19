from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'image',
                    'category', 'user', 'status')


admin.site.register(News, NewsAdmin)
