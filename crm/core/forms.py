from .models import *
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['username','first_name', 'last_name', 'email', 'cargo']


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = ['nome', 'cpf', 'crm', 'uf_crm', 'espec', 'estado', 'cidade',
                  'numero_fixo', 'whatsapp', 'produto']

class ClinicForm(forms.ModelForm):

    class Meta:
        model = Clinic
        fields = ['razao', 'categoria', 'cnpj', 'numero', 'email', 'produto']


class PipeForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = ['titulo', 'descricao', 'status', 'prioridade', 'produto', 'clinica', 'medico', 'valor_total',
                  'data_ini', 'visivel']


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )