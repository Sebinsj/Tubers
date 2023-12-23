from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    
    list_display=('fullname','email',)
    list_display_links=("fullname",'email',)
    search_fields=("fullname","email",)
    list_filter=()
# Register your models here.


admin.site.register(Contact,ContactAdmin)