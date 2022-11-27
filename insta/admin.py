from django.contrib import admin
from insta.models import Gamsung

# admin.site.register(Gamsung)

# class GamsungAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Gamsung, GamsungAdmin)

@admin.register(Gamsung)
class GamsungAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'contents', 'created_at', 'updated_at']
    list_display_links =['subject']