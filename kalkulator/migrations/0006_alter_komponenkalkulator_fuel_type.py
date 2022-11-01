# Generated by Django 4.1 on 2022-10-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0005_alter_komponenkalkulator_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komponenkalkulator',
            name='fuel_type',
            field=models.CharField(choices=[('bensin', 'Bensin'), ('diesel', 'Diesel')], default='Unspecified', max_length=10),
        ),
    ]