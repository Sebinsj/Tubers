from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    
    list_display=('fname','email',)
    list_display_links=("fname",'email',)
    search_fields=("fname","email",)
    list_filter=()
# Register your models here.


admin.site.register(Contact,ContactAdmin)