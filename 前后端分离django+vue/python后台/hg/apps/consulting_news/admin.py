from django.contrib import admin

from .models import ConsultingNews


class ConsultingNewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'release_time',
    )


admin.site.register(ConsultingNews, ConsultingNewsAdmin)