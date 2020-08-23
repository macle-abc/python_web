from django.contrib import admin

from .models import HomeEncyclopedias


class HomeEncyclopediasAdmin(admin.ModelAdmin):
    list_display = (
        'problem',
    )


admin.site.register(HomeEncyclopedias, HomeEncyclopediasAdmin)


