# Generated by Django 4.2.1 on 2023-05-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0026_remove_product_pamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pAmount',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
        ),
    ]
