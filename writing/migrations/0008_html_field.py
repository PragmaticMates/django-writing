# Generated by Django 5.0.9 on 2024-10-04 20:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0007_markdown_to_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='content'),
        ),
    ]
