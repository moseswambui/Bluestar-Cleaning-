# Generated by Django 3.2 on 2022-12-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0023_service_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='pay',
            field=models.CharField(default='Pay During Visit', max_length=200),
        ),
    ]
