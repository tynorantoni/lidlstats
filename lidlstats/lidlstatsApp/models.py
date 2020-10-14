from django.db import models
import datetime


class BasicDataModel(models.Model):
    date_of_shopping = models.DateField(default=datetime.date.today)
    product_data = models.JSONField(default=dict)
    user_mail = models.CharField(max_length=100, default="none@none.none")

    def __repr__(self):
        return str(self.product_data)


class CalculatedDataModel(models.Model):
    shoppig_id = models.IntegerField(null=False)
    date_of_shoppings = models.DateField(default=datetime.date.today)
    total_cost = models.FloatField(default=0.00)
    vat_a = models.FloatField(default=0.00)
    vat_b = models.FloatField(default=0.00)
    vat_c = models.FloatField(default=0.00)
    max_price = models.FloatField(default=0.00)
    min_price = models.FloatField(default=0.00)
    median_cost = models.FloatField(default=0.00)
    mean_cost = models.FloatField(default=0.00)

    def __repr__(self):
        return str(self.total_cost)
