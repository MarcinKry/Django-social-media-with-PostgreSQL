from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import Slider, Team


class TeamAdmin(admin.ModelAdmin):

    def myPhoto(self,object):
        return format_html('<img src = "{}" width="40" />'.format(object.first_name))

    list_display = ('id', 'myPhoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('headline', 'photos', 'button_text')



admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
