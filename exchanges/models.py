from django.db import models

# Create your models here.


class Exchange(models.Model):
    exchange_name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)

    def __str__(self):
        return self.exchange_name


class Order(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    order_coin = models.CharField(max_length=5)
    order_coin_used = models.CharField(max_length=5)
    order_date_created = models.DateField('order created')
    order_date_executed = models.DateField('order executed')
    # TODO: add order properties

    def __str__(self):
        return self.order_coin_used + "-" + self.order_coin
