# Generated by Django 3.0.7 on 2020-11-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20201024_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
