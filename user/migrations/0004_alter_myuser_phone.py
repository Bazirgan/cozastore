# Generated by Django 5.0.1 on 2024-03-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myuser_date_of_brith'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
