# Generated by Django 5.0.1 on 2024-03-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]