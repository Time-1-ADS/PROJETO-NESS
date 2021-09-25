from django.contrib import admin
from core.models import Permission, Agent


class AgentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cargo')
    list_filter = ('cargo', 'nome')


admin.site.register(Permission)
admin.site.register(Agent, AgentAdmin)
