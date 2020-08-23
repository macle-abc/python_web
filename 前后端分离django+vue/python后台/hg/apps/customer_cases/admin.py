from django.contrib import admin

from .models import CustomerCases, CustomerCasesImages, CustomerCasesVideos


class CustomerCasesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name'
    ]


admin.site.register(CustomerCases, CustomerCasesAdmin)
admin.site.register(CustomerCasesImages)
admin.site.register(CustomerCasesVideos)
