# Generated by Django 4.2.11 on 2024-05-14 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='products/'),
            preserve_default=False,
        ),
    ]
