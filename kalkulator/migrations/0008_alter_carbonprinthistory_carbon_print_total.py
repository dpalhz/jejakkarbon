# Generated by Django 4.1 on 2022-10-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0007_remove_komponenkalkulator_tagihan_listrik_rupiah_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbonprinthistory',
            name='carbon_print_total',
            field=models.FloatField(default=0),
        ),
    ]