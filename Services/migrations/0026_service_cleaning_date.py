# Generated by Django 3.2 on 2023-01-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0025_alter_service_service_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cleaning_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]