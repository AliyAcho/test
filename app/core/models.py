from django.db import models

# Create your models here.

class Orders(models.Model):
    index = models.IntegerField(verbose_name="№")
    order_number = models.IntegerField(verbose_name="заказ №")
    dollar_value = models.FloatField(verbose_name="стоимость, $")
    ruble_value = models.FloatField(verbose_name="стоимость в руб.")
    delivery_time = models.DateField(verbose_name="срок поставки")
    
    sending_notification = models.BooleanField(default=False, verbose_name="Отправлялось уведомление?")