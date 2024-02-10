from django.contrib import admin
from core.models import Category, Product, Color


admin.site.register(Category)
admin.site.register(Color)

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

