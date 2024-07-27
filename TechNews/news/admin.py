from django.contrib import admin

from .models import (
    News,
    Tags,
    Resources
)


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'text', 'get_tags', 'get_resources', 'id'
    )

    def get_tags(self, obj):
        return ", ".join([tag.title for tag in obj.tags.all()])

    get_tags.short_description = 'Tags'

    def get_resources(self, obj):
        return ", ".join([resource.title for resource in obj.resources.all()])

    get_resources.short_description = 'Resources'


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
