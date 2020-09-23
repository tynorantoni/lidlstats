# Generated by Django 3.1.1 on 2020-09-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lidlstatsApp', '0002_auto_20200923_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatedDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_id', models.IntegerField()),
                ('total_cost', models.FloatField(default=0.0)),
                ('vat_a', models.FloatField(default=0.0)),
                ('vat_b', models.FloatField(default=0.0)),
                ('vat_c', models.FloatField(default=0.0)),
                ('max_price', models.FloatField(default=0.0)),
                ('min_price', models.FloatField(default=0.0)),
                ('median_cost', models.FloatField(default=0.0)),
                ('mean_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='basicdatamodel',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='basicdatamodel',
            name='vat_a',
        ),
        migrations.RemoveField(
            model_name='basicdatamodel',
            name='vat_b',
        ),
        migrations.RemoveField(
            model_name='basicdatamodel',
            name='vat_c',
        ),
    ]
