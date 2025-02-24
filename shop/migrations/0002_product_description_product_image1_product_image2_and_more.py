# Generated by Django 4.1.3 on 2024-09-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(default="No description available"),
        ),
        migrations.AddField(
            model_name="product",
            name="image1",
            field=models.ImageField(blank=True, null=True, upload_to="product_images"),
        ),
        migrations.AddField(
            model_name="product",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to="product_images"),
        ),
        migrations.AddField(
            model_name="product",
            name="image3",
            field=models.ImageField(blank=True, null=True, upload_to="product_images"),
        ),
        migrations.AddField(
            model_name="product",
            name="image4",
            field=models.ImageField(blank=True, null=True, upload_to="product_images"),
        ),
    ]
