from django.db import models

class stock_params(models.Model):
 id = models.IntegerField(primary_key=True)
 price_profit = models.DecimalField(max_digits=10, decimal_places=2)
 price_sales = models.DecimalField(max_digits=10, decimal_places=2)
 price_cashflow = models.DecimalField(max_digits=10, decimal_places=2)
 price_book_value = models.DecimalField(max_digits=10, decimal_places=2)
 price_ebidta = models.DecimalField(max_digits=10, decimal_places=2)
 name = models.CharField(max_length=10)

class stock_price(models.Model):
 name = models.CharField(max_length=10)
 stock_price = models.DecimalField(max_digits=10, decimal_places=2)
