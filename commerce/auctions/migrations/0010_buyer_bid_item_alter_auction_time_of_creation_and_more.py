# Generated by Django 4.1 on 2022-08-26 23:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_buyer_bid_item_alter_auction_time_of_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='bid_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_bidded_on', to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 19, 43, 39, 682393)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_of_commment',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 19, 43, 39, 682393)),
        ),
    ]
