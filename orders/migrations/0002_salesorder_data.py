# Generated by Django 4.2.2 on 2023-06-11 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
