# Generated by Django 4.0.3 on 2022-03-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_follow_follower_account_followed_accounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='followed_accounts',
        ),
        migrations.AddField(
            model_name='account',
            name='followed_accounts',
            field=models.ManyToManyField(blank=True, related_name='follows', to='users.account'),
        ),
        migrations.RemoveField(
            model_name='account',
            name='follower_accounts',
        ),
        migrations.AddField(
            model_name='account',
            name='follower_accounts',
            field=models.ManyToManyField(blank=True, to='users.account'),
        ),
    ]
