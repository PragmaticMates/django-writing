# Generated by Django 3.1.14 on 2022-04-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0005_article_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='publish_date'),
        ),
    ]