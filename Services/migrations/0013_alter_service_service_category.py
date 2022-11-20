# Generated by Django 4.1.2 on 2022-11-20 11:39

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0012_servicecategory_price_extraserviceinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_category',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='type', on_delete=django.db.models.deletion.CASCADE, to='Services.servicecategory'),
        ),
    ]
