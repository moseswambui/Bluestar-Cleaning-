# Generated by Django 4.1.2 on 2022-11-16 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0008_alter_servicetype_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceapplications',
            name='category',
        ),
        migrations.RemoveField(
            model_name='serviceapplications',
            name='type',
        ),
    ]
