# Generated by Django 3.1.10 on 2021-05-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20210516_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='parent',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]