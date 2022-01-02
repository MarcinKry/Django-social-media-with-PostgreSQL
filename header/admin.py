from django.contrib import admin
from .models import Header
from django.utils.html import format_html
# Register your models here.



class HeaderAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')


admin.site.register(Header, HeaderAdmin)
