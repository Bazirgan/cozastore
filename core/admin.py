from django.contrib import admin
from core.models import (
    Category, Product, Color, Blog, Contact, ContactMail
)

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Contact)
admin.site.register(ContactMail)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'size')
    search_fields = ('name', 'price', 'category__name', 'color__name')
    readonly_fields = ('like',)
    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'price', 'category', 'color', 'size')
        }),
        ('Main Information', {
            'fields': ('like', )
        }),
    )
    ordering = ('-created_at',)
    
admin.site.register(Product,ProductAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description',)
    last_filter = ('created_at',)
    fields = ('title', 'description' ,'slug','is_active', 'image' )
    ordering = ('-created_at',)
    
admin.site.register(Blog,BlogAdmin)

