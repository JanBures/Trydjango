# Generated by Django 2.2.1 on 2019-05-12 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='priceEUR',
        ),
    ]
