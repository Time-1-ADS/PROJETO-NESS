from .models import *
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['nome', 'email', 'senha', 'cargo']


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = ['nome', 'cpf', 'crm', 'uf_crm', 'espec', 'estado', 'cidade',
                  'numero_fixo', 'whatsapp']


class PipeForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = ['nome', 'empresa', 'descricao', 'status', 'valor_total',
                  'data_ini', 'visivel']
