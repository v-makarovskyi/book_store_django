# Generated by Django 4.1.4 on 2022-12-29 17:12

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookstore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="автор")),
                ("genre", models.CharField(max_length=200, verbose_name="жанр")),
                (
                    "about",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Об авторе"
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="* Обязательное поле",
                        max_length=150,
                        verbose_name="Название",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="добавьте изображение книги",
                        upload_to="images/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="описание книги"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("ru", "русский"),
                            ("ua", "украинский"),
                            ("en", "английский"),
                            ("fr", "французский"),
                            ("de", "немецкий"),
                        ],
                        default="русский",
                        max_length=30,
                        verbose_name="язык",
                    ),
                ),
                (
                    "binding",
                    models.CharField(
                        choices=[
                            ("h", "твердый"),
                            ("p", "мягкая обложка"),
                            ("s", "суперобложка"),
                            ("i", "интегральный"),
                            ("c", "картон"),
                            ("l", "кожаный"),
                            ("fc", "обложка с клапанами"),
                        ],
                        max_length=50,
                        verbose_name="переплет",
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        choices=[
                            ("a", "до 4-x"),
                            ("b", "4-6"),
                            ("с", "7-12"),
                            ("d", "12-14"),
                            ("e", "16+"),
                            ("f", "18+"),
                        ],
                        default="18+",
                        max_length=15,
                        verbose_name="возраст",
                    ),
                ),
                (
                    "pages",
                    models.CharField(max_length=10, verbose_name="количество страниц"),
                ),
                (
                    "size",
                    models.CharField(
                        help_text="Укажите физический размер книги",
                        max_length=20,
                        verbose_name="Размеры книги",
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("price", models.CharField(max_length=4, verbose_name="цена")),
                ("discount_price", models.FloatField(blank=True, null=True)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="выберите доступность продукта",
                        verbose_name="доступность продукта",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="создан"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="изменен"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bookstore.author",
                        verbose_name="автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bookstore.category",
                        verbose_name="рубрика",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="BookSpecific",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="укажите название характеристики товара",
                        max_length=1200,
                        verbose_name="название характеристики",
                    ),
                ),
            ],
            options={
                "verbose_name": "Характеристика товара",
                "verbose_name_plural": "Характеристики товара",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="* Обязательное поле",
                        max_length=200,
                        unique=True,
                        verbose_name="тип товара",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Тип товара",
                "verbose_name_plural": "Типы товара",
            },
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Издательство")),
            ],
            options={
                "verbose_name": "Издательство",
                "verbose_name_plural": "Издательства",
            },
        ),
        migrations.CreateModel(
            name="BookSpecificValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        max_length=100, verbose_name="описание характеристики"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookstore.book",
                        verbose_name="Книга",
                    ),
                ),
                (
                    "specification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bookstore.bookspecific",
                        verbose_name="Выберите из списка",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "описание характеристик товара",
            },
        ),
        migrations.AddField(
            model_name="bookspecific",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="bookstore.producttype"
            ),
        ),
        migrations.CreateModel(
            name="BookComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="автор",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bookstore.book"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="bookstore.producttype",
                verbose_name="тип товара",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="bookstore.publisher",
                verbose_name="Издательство",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="user_wishlist",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
