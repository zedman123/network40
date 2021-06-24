# Generated by Django 3.1.10 on 2021-05-12 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='title',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='level',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='lft',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='rght',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=2, editable=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Splitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=150)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='splitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.splitter'),
        ),
    ]