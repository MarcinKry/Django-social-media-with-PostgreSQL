from django.contrib import admin
from .models import Contacttuber, Contacttuber
from django.utils.html import format_html
# Register your models here.



class ContacttuberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email')


admin.site.register(Contacttuber, ContacttuberAdmin)
