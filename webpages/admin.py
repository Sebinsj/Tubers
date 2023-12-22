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
class SliderAdmin(admin.ModelAdmin):
     def sliderphoto(self,object):
        return format_html('<img src="{}" width="48" '.format(object.photo.url))

     list_display=('sliderphoto','headline','button_text',)
     list_display_links=('sliderphoto','headline','button_text',)
     


admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin)