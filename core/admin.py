from django.contrib import admin
from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin
from core.models import (
    Category, Product, Color, Blog, Contact, ContactMail, Setting
)

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Contact)
admin.site.register(ContactMail)
admin.site.register(Setting)

class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'category', 'size')
    search_fields = ('name', 'price', 'category__name', 'color__name')
    readonly_fields = ('like',)
    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'price', 'category', 'color', 'size','image')
        }),
        ('Main Information', {
            'fields': ('like', )
        }),
    )
    ordering = ('-created_at',)
    
admin.site.register(Product,ProductAdmin)


class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description',)
    last_filter = ('created_at',)
    fields = ('title', 'description' ,'slug','is_active', 'image' )
    ordering = ('-created_at',)
    
admin.site.register(Blog,BlogAdmin)

