# Generated by Django 4.2.4 on 2023-09-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='details',
        ),
        migrations.AddField(
            model_name='media',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]