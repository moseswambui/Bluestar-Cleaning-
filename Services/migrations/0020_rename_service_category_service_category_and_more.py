# Generated by Django 4.1.2 on 2022-11-22 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0019_alter_service_consultant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_type',
            new_name='type',
        ),
    ]