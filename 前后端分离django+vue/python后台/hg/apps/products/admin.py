from django.contrib import admin

from .models import Products, ProductsImages


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'style',
        'site',
        'key_word',
    )
    search_fields = (
        'key_word',
    )


class ProductsImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsImages, ProductsImageAdmin)
