# Generated by Django 3.1.10 on 2021-05-12 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210512_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='splitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.splitter'),
        ),
        migrations.AddField(
            model_name='splitter',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='customer.category'),
            preserve_default=False,
        ),
    ]
