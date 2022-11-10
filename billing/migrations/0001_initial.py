# Generated by Django 4.1.2 on 2022-11-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(default='')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('REVERSED', 'REVERSED'), ('PAID', 'PAID')], default='PENDING', max_length=10)),
                ('customer_id', models.CharField(max_length=255, null=True)),
                ('invoice_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('application_submission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Services.serviceapplications')),
            ],
            options={
                'verbose_name': 'Bill',
                'verbose_name_plural': 'Bills',
            },
        ),
    ]
