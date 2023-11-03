# Generated by Django 4.2.7 on 2023-11-03 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_remove_review_email_alter_review_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='post',
            new_name='tours',
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 20, 9, 36, 655189)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 20, 9, 36, 655189)),
        ),
    ]