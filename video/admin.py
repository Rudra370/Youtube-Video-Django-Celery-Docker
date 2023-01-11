from django.contrib import admin
from video.models import Video, Thumbnail

class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ('url', 'width', 'height')
    list_filter = ('width', 'height')
    search_fields = ('url',)
    raw_id_fields = ('video',)

class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    extra = 1

class VideoAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ('title', 'published_at', 'channel_title', 'description')
    list_filter = ('published_at', 'created_at', 'updated_at')
    search_fields = ('title', 'channel_title', 'description')


admin.site.register(Video, VideoAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)