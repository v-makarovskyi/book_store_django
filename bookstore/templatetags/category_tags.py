from django import template
from bookstore.models import Category

register = template.Library()


@register.inclusion_tag('bookstore/include/tags/category_tags_for_bigmenu.html')
def get_categories():
    category = Category.objects.all()
    return {'list_category': category}