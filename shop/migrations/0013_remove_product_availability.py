# Generated by Django 4.2.4 on 2023-09-06 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_product_details_product_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='availability',
        ),
    ]