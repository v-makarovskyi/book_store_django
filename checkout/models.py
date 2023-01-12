from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryOptions(models.Model):
    """ The table contains all valid shipping methods """

    DELIVERY_CHOICES = [
        ('sz', 'Самовывоз из офиса'),
        ('np', 'Новая Почта'),
        ('up', 'УкрПочта'),
    ]

    delivery_title = models.CharField(
        _('метод доставки'), max_length=100, help_text=_('* обязательное поле'))
    delivery_price = models.CharField(_('стоимость доставки'), max_length=30)
    delivery_method = models.CharField(
        _('вариант доставки'), choices=DELIVERY_CHOICES, max_length=255, help_text=_('* обязательно'))

    class Meta:
        verbose_name = _('Опция доставки')
        verbose_name_plural = _('Опции доставок')

    def __str__(self) -> str:
        return self.delivery_title



class PaymentOptions(models.Model):
    """ The table contains all valid payment methods """

    PAYMENT_CHOICES = [
        ('c', 'Наличными'),
        ('ba', 'Банковской картой'),
        ('p', 'На карту Приват'),
        ('ba', 'Перевод на рассчетный счет'),
    ]

    payment_title = models.CharField(
        _('метод оплаты'), max_length=100, help_text=_('* обязательное поле'))
    payment_method = models.CharField(
        _('вариант оплаты'), choices=PAYMENT_CHOICES, max_length=255, help_text=_('* обязательно'))

    class Meta:
        verbose_name = _('Опция платежа')
        verbose_name_plural = _('Опции платежей')

    def __str__(self) -> str:
        return self.payment_title


