# Generated by Django 5.1.6 on 2025-02-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='warehouse_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
