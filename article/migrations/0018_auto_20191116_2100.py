# Generated by Django 2.1.7 on 2019-11-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '列表', 'verbose_name_plural': '列表'},
        ),
        migrations.AlterModelOptions(
            name='articletype',
            options={'verbose_name': '类型', 'verbose_name_plural': '类型'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.CharField(default='', max_length=100, verbose_name='概述'),
        ),
    ]