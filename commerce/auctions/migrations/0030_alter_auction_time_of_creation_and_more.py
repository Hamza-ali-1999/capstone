# Generated by Django 4.1 on 2022-08-31 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_alter_auction_time_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 4, 45, 2, 944434)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_of_commment',
            field=models.CharField(default='08/31/2022, 04:45:03', max_length=200),
        ),
    ]
