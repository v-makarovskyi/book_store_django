from django.db import models
from django.conf import settings
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
    
    name = models.CharField('рубрика', max_length=100, help_text='* название основной рубрики книг')
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    
