from django.contrib.admin import ModelAdmin, TabularInline, register, site
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import AmountIngredient, Ingredient, Recipe, Tag
from import_export import resources
site.site_header = 'Администрирование Foodgram'
EMPTY_VALUE_DISPLAY = 'Значение не указано'


class IngredientInline(TabularInline):
    model = AmountIngredient
    extra = 2


@register(AmountIngredient)
class LinksAdmin(ModelAdmin):
    pass


class IngredientResource(resources.ModelResource):

    class Meta:
        model = Ingredient


@register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin, ModelAdmin):
    resource_classes = [IngredientResource]
    list_display = (
        'name', 'measurement_unit',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'name',
        'author',
        'get_image',
    )
    fields = (
        ('name', 'cooking_time',),
        ('author', 'tags',),
        ('text',),
        ('image',),
    )
    raw_id_fields = ('author', )
    search_fields = (
        'name', 'author', 'tags'
    )
    list_filter = (
        'name', 'author__username', 'tags',
    )

    inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" hieght="30"')

    get_image.short_description = 'Изображение'


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'name', 'color', 'slug',
    )
    search_fields = (
        'name', 'color'
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY
