# Generated by Django 3.1.14 on 2022-03-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0004_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(blank=True, db_index=True, max_length=2, verbose_name='language'),
        ),
    ]
