# Generated by Django 4.1.5 on 2024-01-22 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_alter_venta_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='producto',
        ),
    ]
