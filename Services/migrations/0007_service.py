# Generated by Django 4.1.2 on 2022-11-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_rename_variation_servicevariation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField(blank=True, null=True)),
                ('service_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.servicecategory')),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.servicetype')),
            ],
        ),
    ]