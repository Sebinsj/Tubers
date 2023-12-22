from django.contrib import admin
from .models import Hiretuber

# Register your models here.
class HiretuberAdmin(admin.ModelAdmin):
    
    list_display=('first_name','email',)
    list_display_links=("first_name",'email',)
    search_fields=("first_name","last_name")
    list_filter=()






admin.site.register(Hiretuber,HiretuberAdmin)