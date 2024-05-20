# Generated by Django 4.2.11 on 2024-05-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spotlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='', verbose_name='spotlight/')),
                ('product_name', models.CharField(max_length=50)),
                ('offer', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='', verbose_name='spotlight/')),
            ],
        ),
    ]