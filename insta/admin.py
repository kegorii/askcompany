from django.contrib import admin
from insta.models import Gamsung
from django.utils.safestring import mark_safe

# admin.site.register(Gamsung)

# class GamsungAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Gamsung, GamsungAdmin)

@admin.register(Gamsung)
class GamsungAdmin(admin.ModelAdmin):

    list_display = ['id','photo_tag', 'subject', 'contents_abbr', 'is_public' ,'created_at', 'updated_at']
    list_display_links =['subject']
    search_fields = ['subject','contents']
    list_filter = ['created_at', 'is_public']

    def contents_abbr(self, post):
        abbr_contents = post.contents[0:35]
        if len(post.contents) > 35:
            return abbr_contents + ' ...'
        else : 
            return abbr_contents    

    contents_abbr.short_description = '컨텐츠 요약'    

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px"/>')
        return None    