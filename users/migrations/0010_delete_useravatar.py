# Generated by Django 2.1.7 on 2019-08-23 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_useravatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAvatar',
        ),
    ]