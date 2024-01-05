from django.contrib import admin
from .models import Hiretuber

# Register your models here.
class HiretuberAdmin(admin.ModelAdmin):
    
    list_display=('firstname','email',"tuber_name")
    list_display_links=("firstname",'email',"tuber_name")
    search_fields=("firstname","last_name")
    list_filter=()






admin.site.register(Hiretuber,HiretuberAdmin)