# Generated by Django 3.0.7 on 2020-10-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]