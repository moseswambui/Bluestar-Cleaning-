# Generated by Django 3.2 on 2022-11-29 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0021_auto_20221125_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='serviceinfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.extraserviceinfo'),
        ),
    ]