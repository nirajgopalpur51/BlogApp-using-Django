from django.contrib import admin
# from django.contrib.sites.models import Site
from .models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']


# class CustomSiteAdmin(admin.AdminSite):
#     site_header = "Bookmark Admin"
#     site_title = "Bookmark site"
#     index_title = "Welcome to the bookmark admin"


# custom_admin_site = CustomSiteAdmin(name="customadmin")
# custom_admin_site.register(Site)
