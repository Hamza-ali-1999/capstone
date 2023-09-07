# Generated by Django 4.1 on 2022-09-01 01:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_alter_auction_time_of_creation_alter_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 21, 38, 56, 311891)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default='08/31/2022, 21:38:56', max_length=200),
        ),
        migrations.CreateModel(
            name='AuctionWinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('auction_closer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_holder', to=settings.AUTH_USER_MODEL)),
                ('closed_auction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_that_has_finished', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
