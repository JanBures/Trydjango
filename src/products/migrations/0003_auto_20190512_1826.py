# Generated by Django 2.2.1 on 2019-05-12 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_priceeur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='priceCZK',
            new_name='price',
        ),
    ]
