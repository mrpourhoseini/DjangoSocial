from django.contrib import admin

from apps.social.models import Post, Profile, Comment, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)
