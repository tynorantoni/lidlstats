# Generated by Django 3.1.1 on 2020-09-17 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_shopping', models.DateField(default=datetime.date.today)),
                ('product_data', models.JSONField(default=dict)),
                ('user_mail', models.CharField(default='none@none.none', max_length=100)),
                ('total_cost', models.FloatField(default=0.0)),
                ('vat_a', models.FloatField(default=0.0)),
                ('vat_b', models.FloatField(default=0.0)),
                ('vat_c', models.FloatField(default=0.0)),
            ],
        ),
    ]