# Generated by Django 4.2.4 on 2023-09-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='details',
            field=models.TextField(blank=True, verbose_name='Details'),
        ),
    ]