# Generated by Django 4.2.3 on 2023-11-03 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_rename_region_address_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Область', 'verbose_name_plural': 'Области'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
    ]
