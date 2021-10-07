from django.contrib import admin
from core.models import *


class AgentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cargo', 'foto')
    list_filter = ('cargo', 'nome')


class MedicAdmin(admin.ModelAdmin):
    list_display = ('nome', 'espec', 'estado')
    list_filter = ('espec', 'estado', 'cidade')


class PipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'status')


admin.site.register(Permission)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Medic, MedicAdmin)
admin.site.register(Clinic)
admin.site.register(Pipeline, PipeAdmin)
