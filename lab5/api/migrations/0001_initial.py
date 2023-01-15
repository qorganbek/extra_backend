# Generated by Django 4.1.5 on 2023-01-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('number', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]