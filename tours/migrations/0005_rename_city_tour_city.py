# Generated by Django 4.2.3 on 2023-10-30 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tour_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='City',
            new_name='city',
        ),
    ]
