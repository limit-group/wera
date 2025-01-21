from django.contrib import admin

from wera.models import Category, Location, Wera


@admin.register(Wera)
class WeraAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "location", "category")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image)
        return "-"
    image_preview.short_description = "Image Preview"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
