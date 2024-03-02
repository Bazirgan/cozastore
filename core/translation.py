from modeltranslation.translator import translator, TranslationOptions

from core.models import (
    Category,
    Color,
    Product,
    Blog,
    Contact,
    ContactMail,
)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)
    
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)
    
class BlogTranslationOptions(TranslationOptions):
    fields = ('slug',)
    
class ContactTranslationOptions(TranslationOptions):
    fields = ('adress',)
    
class ContactMailTranslationOptions(TranslationOptions):
    fields = ('email',)
    
translator.register(Category, CategoryTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(ContactMail, ContactMailTranslationOptions)
