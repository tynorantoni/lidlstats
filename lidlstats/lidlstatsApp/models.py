from django.db import models
import datetime


class BasicDataModel(models.Model):
    date_of_shopping = models.DateField(default=datetime.date.today)
    product_data = models.JSONField(default=dict)
    user_mail = models.CharField(max_length=100, default="none@none.none")
    total_cost = models.FloatField(default=0.00)
    vat_a = models.FloatField(default=0.00)
    vat_b = models.FloatField(default=0.00)
    vat_c = models.FloatField(default=0.00)

    def __str__(self):
        return self.product_data
