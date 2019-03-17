# Generated by Django 2.1.7 on 2019-03-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='home_size',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='last_sold_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='property_size',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rentzestimate_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='tax_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='tax_year',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='year_built',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zestimate_amount',
            field=models.FloatField(null=True),
        ),
    ]
