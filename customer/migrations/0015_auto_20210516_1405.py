# Generated by Django 3.1.10 on 2021-05-16 12:05

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20210516_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='customer.customer'),
        ),
    ]