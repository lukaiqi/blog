# Generated by Django 2.1.7 on 2019-08-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190811_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='邮箱'),
        ),
    ]
