from django.db import models
from django.conf import settings
from bookstore.models import Book
from account.models import Address
from checkout.models import DeliveryOptions, PaymentOptions


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f'{self.quantity} : {self.item.title}'

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.get_discount_price()

    def get_final_price(self):
        if self.item.discount:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='order_user')
    items = models.ManyToManyField(OrderItem, verbose_name='позиции заказа')
    shipping_address = models.ForeignKey(
        Address, verbose_name='Адрес доставки', on_delete=models.RESTRICT, related_name='shipping_address')
    delivery_options = models.ForeignKey(
        DeliveryOptions, verbose_name='метод доставки', on_delete=models.RESTRICT, related_name='delivery_options')
    payment_options = models.ForeignKey(
        PaymentOptions, verbose_name='метод оплаты', on_delete=models.RESTRICT, related_name='payment_options')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.user.username
    
    def det_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total