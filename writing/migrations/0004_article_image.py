# Generated by Django 2.2.4 on 2020-07-07 09:34

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0003_auto_20200608_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='photo or image', max_length=1024, upload_to='images', verbose_name='image'),
        ),
    ]
