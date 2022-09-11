from django.contrib import admin

from .models import *

admin.site.site_header = 'Percula CanaryLink'

class CanarySettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(CanaryString)
admin.site.register(CanaryFile,)
admin.site.register(CanarySetting, CanarySettingAdmin)
