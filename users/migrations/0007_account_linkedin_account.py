# Generated by Django 4.0.3 on 2022-03-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_group_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='linkedin_account',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
