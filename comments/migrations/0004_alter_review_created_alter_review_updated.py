# Generated by Django 4.2.7 on 2023-11-03 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_review_options_remove_review_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 19, 49, 32, 57700)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 19, 49, 32, 57700)),
        ),
    ]