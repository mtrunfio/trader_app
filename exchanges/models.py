from django.db import models


class Exchange(models.Model):
    exchange_name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)

    def __str__(self):
        return self.exchange_name

    def add_exchange(self, exchange_name, api_key, secret):
        try:
            if(exchange_name == ""):
                return "error", "Exchange name is required"

            if(api_key == ""):
                return 'error', 'API Key is required'

            if(secret == ""):
                return 'error', 'Secret is required'

            new_exchange = Exchange(
                exchange_name=exchange_name, api_key=api_key, secret=secret)
            new_exchange.save()

            return new_exchange
        except Exception as ex:
            return ex

    def delete_exchange(self, exchange_id):
        try:
            Exchange.objects.get(pk=exchange_id).delete()
            return "success", "Exchange deleted succesfully"

        except Exception as ex:
            return "error", ex

    def update_exchange(self, exchange_id, values):
        try:
            if values['exchange_name'] == "":
                return "error", "Exchange name cannot be blank" 

            if values['api_key'] == "":
                return "error", "Api key cannot be blank" 

            if values['secret'] == "":
                return "error", "Secret cannot be blank" 

            ex = Exchange.objects.get(pk=exchange_id)
            ex.exchange_name = values['exchange_name']
            ex.api_key = values['api_key']
            ex.secret = values['secret']
            ex.save()
            return "success", "Exchange updated succesfully"

        except Exception as ex:
            return "error", ex


class Order(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    order_coin = models.CharField(max_length=5)
    order_coin_used = models.CharField(max_length=5)
    order_date_created = models.DateField('order created')
    order_date_executed = models.DateField('order executed')
    # TODO: add order properties

    def __str__(self):
        return self.order_coin_used + "-" + self.order_coin
