from .models import *
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['nome', 'email', 'senha', 'cargo']
