# Generated by Django 4.0.3 on 2022-03-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_follow_follow_follower_follow_followed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.AddField(
            model_name='account',
            name='followers_account',
            field=models.ManyToManyField(blank=True, to='users.follow'),
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.AddField(
            model_name='follow',
            name='followed',
            field=models.ManyToManyField(blank=True, to='users.account'),
        ),
    ]
