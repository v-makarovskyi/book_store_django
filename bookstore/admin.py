from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Book,
    BookComment,
    BookSpecific,
    BookSpecificValue,
    ProductType,
    Author,
    Publisher,
)

admin.site.register(Category, MPTTModelAdmin)

class BookSpecificInline(admin.TabularInline):
    model = BookSpecific

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [BookSpecificInline]

@admin.register(Publisher)
class PubliserAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

class BookSpecificValueInline(admin.TabularInline):
    model = BookSpecificValue

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookSpecificValueInline]
    list_display = ['id', 'title', 'author', 'category', 'price']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)