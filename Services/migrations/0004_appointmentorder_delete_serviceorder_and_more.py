# Generated by Django 4.1.2 on 2022-11-12 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_rename_service_serviceorder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('category', models.CharField(blank=True, max_length=250, null=True)),
                ('service', models.CharField(blank=True, max_length=250, null=True)),
                ('consultant', models.CharField(blank=True, max_length=250, null=True)),
                ('appointment_date', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.DeleteModel(
            name='ServiceOrder',
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='Services.servicetype'),
        ),
    ]
