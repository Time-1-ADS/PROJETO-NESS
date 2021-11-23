from django.contrib import admin
from core.models import *


# class AgentAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'email', 'cargo', 'foto')
#     list_filter = ('cargo', 'nome')


class MedicAdmin(admin.ModelAdmin):
    list_display = ('nome', 'espec', 'estado')
    list_filter = ('espec', 'estado', 'cidade')


class PipeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'status')

class TituloMainAdmin(admin.ModelAdmin):
    list_display = ('novo', 'aberto', 'pendente', 'fechado')


admin.site.register(Permission)
# admin.site.register(Agent, AgentAdmin)
admin.site.register(Medic, MedicAdmin)
admin.site.register(Clinic)
admin.site.register(Pipeline, PipeAdmin)
admin.site.register(Empresa)
admin.site.register(TituloMain, TituloMainAdmin)