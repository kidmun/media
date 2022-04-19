# Generated by Django 4.0.3 on 2022-04-19 00:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_account_email'),
        ('actions', '0006_alter_groupmessage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('body', models.CharField(blank=True, max_length=1000, null=True)),
                ('post_image', models.ImageField(blank=True, default='post_images/default.jpg', null=True, upload_to='post_images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.account')),
            ],
        ),
    ]