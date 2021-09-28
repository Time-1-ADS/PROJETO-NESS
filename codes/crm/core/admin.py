from django.contrib import admin
from core.models import *


class AgentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cargo')
    list_filter = ('cargo', 'nome')


class MedicAdmin(admin.ModelAdmin):
    list_display = ('nome', 'espec', 'estado')
    list_filter = ('espec', 'estado', 'cidade')


admin.site.register(Permission)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Medic, MedicAdmin)
