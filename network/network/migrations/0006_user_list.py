# Generated by Django 4.1 on 2023-07-11 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_rename_user_followinglist_list_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following_list', to='network.followinglist'),
        ),
    ]
