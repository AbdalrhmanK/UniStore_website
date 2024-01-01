# Generated by Django 4.2.1 on 2023-05-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0017_rename_pamount0_product_pamount00'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pAmount00',
        ),
        migrations.AddField(
            model_name='product',
            name='pAmount11',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
