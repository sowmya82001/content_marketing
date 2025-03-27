from django.contrib import admin
from .models import Blog
from .models import SocialMedia
from .models import Contact

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'profile_url')

admin.site.register(Contact)
