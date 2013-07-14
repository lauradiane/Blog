from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

# This tells the admin site to pay attention to this model
admin.site.register(Post, PostAdmin)