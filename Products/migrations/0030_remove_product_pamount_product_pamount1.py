# Generated by Django 4.2.1 on 2023-05-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0029_alter_product_pamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pAmount',
        ),
        migrations.AddField(
            model_name='product',
            name='pAmount1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
