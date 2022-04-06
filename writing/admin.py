from django import forms
from writing import settings as writing_settings
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from writing.models import Category, Article

admin.site.register(Category, DraggableMPTTAdmin,
    search_fields=('title',),
    list_display=('tree_actions', 'indented_title', 'slug', 'created'),
    list_display_links=('indented_title',),
)


class ArticleAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].widget = forms.Select(choices=writing_settings.LANGUAGES)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category__title', 'excerpt', 'content')
    date_hierarchy = 'created'
    list_display = ('title', 'category', 'language', 'author', 'is_highlighted', 'is_published', 'publish_date', 'created', 'modified')
    list_filter = ('is_highlighted', 'is_published', 'language', ('category', TreeRelatedFieldListFilter))
    list_editable = ('is_highlighted', 'is_published')
    list_select_related = ['category', 'author']
    raw_id_fields = ['author']
    # autocomplete_fields = ['category', 'author']

    form = ArticleAdminForm
