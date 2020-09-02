from django.contrib import admin

# Register your models here.

from .models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['person', 'subject', 'date']

admin.site.register(Agenda, AgendaAdmin)