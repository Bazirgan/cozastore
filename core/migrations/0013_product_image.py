# Generated by Django 5.0.1 on 2024-02-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='media/shop/'),
            preserve_default=False,
        ),
    ]