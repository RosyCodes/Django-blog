from django.contrib import admin
from .models import About, SocialLink

# Overrides the admin panel to only add one record


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
