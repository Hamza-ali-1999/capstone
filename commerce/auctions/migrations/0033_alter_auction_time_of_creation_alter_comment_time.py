# Generated by Django 4.1 on 2022-08-31 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_alter_auction_time_of_creation_alter_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 15, 19, 47, 288961)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default='08/31/2022, 15:19:47', max_length=200),
        ),
    ]
