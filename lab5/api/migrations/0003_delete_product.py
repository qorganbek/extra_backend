# Generated by Django 4.1.5 on 2023-01-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]