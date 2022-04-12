# Generated by Django 4.0.3 on 2022-03-29 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_follow_follower_account_followers_account_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='followers_account',
        ),
        migrations.AddField(
            model_name='follow',
            name='followers_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follows', to='users.account'),
        ),
    ]
