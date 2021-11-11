from .models import *
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [ 'cargo']


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = ['nome', 'cpf', 'crm', 'uf_crm', 'espec', 'estado', 'cidade',
                  'numero_fixo', 'whatsapp', 'produto']


class PipeForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = ['titulo', 'empresa', 'descricao', 'status', 'prioridade', 'produto', 'clinica', 'medico', 'valor_total',
                  'data_ini', 'visivel']
