# Generated by Django 3.2.8 on 2021-11-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='copasst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
            ],
        ),
    ]