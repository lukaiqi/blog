# Generated by Django 2.1.7 on 2020-03-05 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilibili', '0006_auto_20200302_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videolist',
            name='url',
        ),
    ]
