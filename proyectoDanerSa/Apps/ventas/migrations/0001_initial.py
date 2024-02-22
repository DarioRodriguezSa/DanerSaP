# Generated by Django 4.1.5 on 2024-01-16 06:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0005_alter_producto_existencia'),
        ('clientes', '0002_alter_cliente_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagada', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'EstadoCuenta',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.FloatField(default=0)),
                ('anticipo', models.FloatField(default=0)),
                ('estado_cuenta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.estadocuenta')),
                ('id_clientes', models.ForeignKey(db_column='id_clientes', on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
            ],
            options={
                'db_table': 'Venta',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.producto')),
                ('venta', models.ForeignKey(db_column='venta', on_delete=django.db.models.deletion.DO_NOTHING, to='ventas.venta')),
            ],
            options={
                'db_table': 'DetalleVenta',
            },
        ),
    ]
