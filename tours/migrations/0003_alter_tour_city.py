# Generated by Django 4.2.3 on 2023-10-30 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_tour_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='City',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.city'),
        ),
    ]
