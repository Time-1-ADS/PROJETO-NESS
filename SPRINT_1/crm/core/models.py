from django.db import models
from django.urls import reverse


class Agent(models.Model):

    nome = models.CharField('Name', max_length=20, help_text='Type the name of Agent.', null=False)
    email = models.EmailField('E-mail', help_text='Type the Agent email address.', null=False)
    senha = models.CharField('Password', max_length=255, null=False)
    cargo = models.ForeignKey('Permission', on_delete=models.CASCADE)
    foto = models.ImageField('Image', upload_to='static/img')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('Profile', args=[str(self.id)])


class Permission(models.Model):
    administrador = 'ADM'
    diretoria = 'DIRETOR'
    sales = 'AGENT'
    cargo_choices = (
        (administrador, 'Administrador'),
        (diretoria, 'Diretor'),
        (sales, 'Agente')
    )
    cargo = models.CharField('Roles', max_length=7, choices=cargo_choices, default=sales)

    def __str__(self):
        return self.cargo

