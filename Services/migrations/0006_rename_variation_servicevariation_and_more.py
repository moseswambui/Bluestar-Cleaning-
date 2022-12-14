# Generated by Django 4.1.2 on 2022-11-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_variation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variation',
            new_name='ServiceVariation',
        ),
        migrations.AlterModelOptions(
            name='servicevariation',
            options={'verbose_name': 'Service Variation', 'verbose_name_plural': 'Service Variations'},
        ),
        migrations.CreateModel(
            name='TechnicianVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('technician', 'technician')], max_length=100)),
                ('variation_value', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.servicecategory')),
            ],
            options={
                'verbose_name': 'Technician Variation',
                'verbose_name_plural': 'Technician Variations',
            },
        ),
    ]
