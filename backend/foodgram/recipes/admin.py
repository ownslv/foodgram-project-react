from django.contrib import admin

from .models import Ingredient, Recipe, Tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
    )
    list_filter = ('author', 'name', 'tags',)


class IngredientResource(resources.ModelResource):

    class Meta:
        model = Ingredient


class IngredientAdmin(ImportExportModelAdmin):
    resource_classes = [IngredientResource]
    list_display = (
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('measurement_unit',)


admin.site.register(Tag)

admin.site.register(Ingredient, IngredientAdmin)
