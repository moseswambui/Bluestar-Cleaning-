# Generated by Django 3.2 on 2023-01-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0027_service_date_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cleaning_date',
        ),
        migrations.AddField(
            model_name='service',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
