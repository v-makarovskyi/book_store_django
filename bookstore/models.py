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
    

class ProductType(models.Model):
    """Типы товаров, представленных на сайте"""

    name = models.CharField('тип товара', max_length=200, unique=True, help_text='* Обязательное поле')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    """Издательство"""

    name = models.CharField('Издательство', max_length=150)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name

class ProductSpecific(models.Model):
    """Модель названий спецификаций и свойств товара"""

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField('название характеристики', max_length=1200, help_text='укажите название характеристики товара')

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'

    def __str__(self):
        return self.name

class ProductSpecificValue(models.Model):
     """Модель значений спецификаций и свойств товара"""