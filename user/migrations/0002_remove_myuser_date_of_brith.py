# Generated by Django 5.0.1 on 2024-03-04 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_brith',
        ),
    ]