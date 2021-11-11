from core.models import Agent
from django import forms



class CadastrarUsuario(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name', 'email', 'password','cargo']