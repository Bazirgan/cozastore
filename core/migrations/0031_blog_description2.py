# Generated by Django 5.0.1 on 2024-04-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_product_image_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description2',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]