# Generated by Django 3.1.10 on 2021-05-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_customer_gps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
