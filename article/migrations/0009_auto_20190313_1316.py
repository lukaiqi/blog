# Generated by Django 2.1.7 on 2019-03-13 13:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0008_auto_20190228_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article_type', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
