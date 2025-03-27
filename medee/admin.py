# news/admin.py

from django.contrib import admin
from .models import News, Category

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the list view
    search_fields = ('name',)  # Search by category name
    ordering = ('id',)  # Ordering of the categories

# Register the News model
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'views')  # Fields to display in the list view
    list_filter = ('category',)  # Add a filter sidebar for categories
    search_fields = ('title', 'author', 'description')  # Fields to search by
    ordering = ('-created_at',)  # Order by created_at, descending
    date_hierarchy = 'created_at'  # Add a date-based hierarchy filter
    readonly_fields = ('views',)  # Make the views field readonly
    
    # Show image in the list view
    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100"/>'
        return None
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Image'

