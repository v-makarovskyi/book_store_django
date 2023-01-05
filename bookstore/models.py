from django.db import models
from django.conf import settings
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Category(MPTTModel):
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    name = models.CharField('рубрика', max_length=100,
                            help_text='* название основной рубрики книг')
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL,
                            blank=True, null=True, related_name='children')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductType(models.Model):
    """Типы товаров, представленных на сайте"""

    name = models.CharField('тип товара', max_length=200,
                            unique=True, help_text='* Обязательное поле')
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


class Author(models.Model):
    name = models.CharField('автор', max_length=200)
    genre = models.CharField('жанр', max_length=200)
    about = RichTextUploadingField('Об авторе')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class BookSpecific(models.Model):
    """Модель названий спецификаций и свойств товара"""

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField('название характеристики', max_length=1200,
                            help_text='укажите название характеристики товара')

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'

    def __str__(self):
        return self.name


class Book(models.Model):

    LANGUAGE_CHOICES = (
        ('ru', 'русский'),
        ('ua', 'украинский'),
        ('en', 'английский'),
        ('fr', 'французский'),
        ('de', 'немецкий'),
    )

    BINDING_CHOICES = (
    ('h', 'твердый'),
    ('p', 'мягкая обложка'),
    ('s', 'суперобложка'),
    ('i', 'интегральный'),
    ('c', 'картон'),
    ('l', 'кожаный'),
    ('fc', 'обложка с клапанами'),
    )

    AGE_CHOICES = (
    ('a', 'до 4-x'),
    ('b', '4-6'),
    ('с', '7-12'),
    ('d', '12-14'),
    ('e', '16+'),
    ('f', '18+'),
    )


    category = models.ForeignKey(
        Category, verbose_name='рубрика', on_delete=models.RESTRICT)
    product_type = models.ForeignKey(
        ProductType, verbose_name='тип товара', on_delete=models.RESTRICT)
    publisher = models.ForeignKey(
        Publisher, verbose_name='Издательство', on_delete=models.RESTRICT)
    author = models.ForeignKey(
        Author, verbose_name='автор', on_delete=models.RESTRICT)
    title = models.CharField('Название', max_length=150,
                         help_text='* Обязательное поле')
    image = models.ImageField(
        'изображение', help_text='добавьте изображение книги', upload_to='images/')
    description = RichTextUploadingField('описание книги')
    language = models.CharField(
        'язык', max_length=30, choices=LANGUAGE_CHOICES, default='русский')
    binding = models.CharField(
        'переплет', max_length=50, choices=BINDING_CHOICES)
    age = models.CharField('возраст', max_length=15,
                       choices=AGE_CHOICES, default='18+')
    pages = models.CharField('количество страниц', max_length=10)
    size = models.CharField('Размеры книги', max_length=20,
                        help_text='Укажите физический размер книги')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.CharField('цена', max_length=4)
    discount_price = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(
        'доступность продукта', help_text='выберите доступность продукта', default=True)
    created = models.DateTimeField('создан', auto_now_add=True, editable=True)
    updated = models.DateTimeField('изменен', auto_now=True)
    user_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookstore:single_book', kwargs={'slug': self.category.slug, 'book_slug': self.slug})

    def add_to_cart(self):
        return reverse('orders:add_to_cart', kwargs={'slug': self.category.slug, 'book_slug': self.slug})


class BookSpecificValue(models.Model):
    """Модель значений спецификаций и свойств товара"""
    book = models.ForeignKey(Book, verbose_name='Книга',
                             on_delete=models.CASCADE)
    specification = models.ForeignKey(
        BookSpecific, verbose_name='Выберите из списка', on_delete=models.RESTRICT)
    value = models.CharField('описание характеристики', max_length=100)

    class Meta:
        verbose_name_plural = 'описание характеристик товара'

    def __str__(self):
        return ('выберите из списка')


class BookComment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='автор', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
