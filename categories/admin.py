from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'details', 'status')


admin.site.register(Category, CategoryAdmin)

