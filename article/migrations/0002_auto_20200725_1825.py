# Generated by Django 3.0.6 on 2020-07-25 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleType', verbose_name='文章分类'),
        ),
    ]