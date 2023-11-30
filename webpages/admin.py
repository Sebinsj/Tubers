from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" '.format(object.photo.url))


    list_display=('id','myphoto','firstname','lastname','created_date')
    list_display_links=("firstname",'myphoto',)
    search_fields=("firstname","role")
    list_filter=("role",)

admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)