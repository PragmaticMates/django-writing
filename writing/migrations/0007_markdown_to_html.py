from django.conf import settings
from django.db import migrations, models
from martor.templatetags.martortags import safe_markdown
from writing.models import Article


def markdown_to_html(apps, schema_editor):
    Article = apps.get_model('writing', 'Article')

    articles = Article.objects.all()

    for article in articles:
        _migrate_content(article)

    Article.objects.bulk_update(articles, fields=['content'])


def _migrate_content(article):
    content_martor = article.content
    content_html = safe_markdown(content_martor)
    article.content = content_html


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0006_article_publish_date'),
    ]

    operations = [
        migrations.RunPython(markdown_to_html),
    ]
