from django.contrib import admin
from .models import Hiretuber
from django.utils.html import format_html
# Register your models here.



class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'user_id', 'tuber_name')


admin.site.register(Hiretuber, HiretuberAdmin)
