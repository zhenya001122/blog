# Generated by Django 4.0.6 on 2022-08-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_color_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='external_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]