# Generated by Django 4.1.5 on 2024-01-19 06:38

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
    ]
