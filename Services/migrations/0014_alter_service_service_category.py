# Generated by Django 4.1.2 on 2022-11-20 11:39

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0013_alter_service_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_category',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='type', null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.servicecategory'),
        ),
    ]
