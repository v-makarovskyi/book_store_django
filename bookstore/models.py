from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey



class Category(models.Model):
    title = models.CharField('категория', max_length=100)
    slug = models.SlugField(max_length=150)
    parent = TreeForeignKey('self', related_name='children',
                            on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    title = models.CharField('тег', max_length=30)
    slug = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Book(models.Model):
    title = models.CharField('название', max_length=200)
    author = models.CharField('автор', max_length=150)
    image = models.ImageField('изображение', upload_to='articles')
    description = RichTextUploadingField()
    slug = models.SlugField(max_length=255)
    price = models.DecimalField('регулярная цена', help_text='max 9999.99', max_digits=7, decimal_places=2, error_messages={
                                'name': {'max_length': 'Цена должна быть в диапазоне от 1 грн до 9999.99 грн'}})
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
