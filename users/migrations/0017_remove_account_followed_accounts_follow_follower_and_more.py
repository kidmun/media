# Generated by Django 4.0.3 on 2022-03-29 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_follow_followed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='followed_accounts',
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.account'),
        ),
        migrations.RemoveField(
            model_name='account',
            name='follower_accounts',
        ),
        migrations.AddField(
            model_name='account',
            name='follower_accounts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.account'),
        ),
    ]
