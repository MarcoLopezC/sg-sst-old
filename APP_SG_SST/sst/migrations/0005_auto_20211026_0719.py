# Generated by Django 3.2.8 on 2021-10-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sst', '0004_rename_rol_name_rol_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cellphone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='identity_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(),
        ),
    ]