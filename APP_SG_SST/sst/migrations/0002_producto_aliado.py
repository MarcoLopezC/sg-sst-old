# Generated by Django 3.2.8 on 2021-11-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto_aliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aliado', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('seguridad_producto', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]