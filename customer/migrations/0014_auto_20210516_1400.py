# Generated by Django 3.1.10 on 2021-05-16 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_customer_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='splitter',
        ),
        migrations.RemoveField(
            model_name='splitter',
            name='w2',
        ),
        migrations.AddField(
            model_name='customer',
            name='splitter32',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.category'),
        ),
    ]