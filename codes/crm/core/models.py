from django.db import models
from django.urls import reverse


class Agent(models.Model):

    nome = models.CharField('Name', max_length=20, null=False)
    email = models.EmailField('E-mail', null=False)
    senha = models.CharField('Password', max_length=255, null=False)
    cargo = models.ForeignKey('Permission', on_delete=models.CASCADE)
    foto = models.ImageField('Image', upload_to='static/img', null=True)

    def __str__(self):
        return self.nome


class Permission(models.Model):
    administrador = 'Administrador'
    diretoria = 'Diretor'
    sales = 'Agente'
    cargo_choices = (
        (administrador, 'ADMINISTRADOR'),
        (diretoria, 'DIRETOR'),
        (sales, 'AGENT')
    )
    cargo = models.CharField('Roles', max_length=13, choices=cargo_choices, default=sales)

    def __str__(self):
        return self.cargo


class Medic(models.Model):
    estados = (('Acre', 'AC'),
               ('Alagoas', 'AL'),
               ('Amapá', 'AP'),
               ('Amazonas', 'AM'),
               ('Bahia', 'BA'),
               ('Ceará', 'CE'),
               ('Espírito Santo', 'ES'),
               ('Goiás', 'GO'),
               ('Maranhão', 'MA'),
               ('Mato Grosso', 'MT'),
               ('Mato Grosso do Sul', 'MS'),
               ('Minas Gerais', 'MG'),
               ('Pará', 'PA'),
               ('Paraíba', 'PB'),
               ('Paraná', 'PR'),
               ('Pernambuco', 'PE'),
               ('Piauí', 'PI'),
               ('Rio de Janeiro', 'RJ'),
               ('Rio Grande do Norte', 'RN'),
               ('Rio Grande do Sul', 'RS'),
               ('Rondônia', 'RO'),
               ('Roraima', 'RR'),
               ('Santa Catarina', 'SC'),
               ('São Paulo', 'SP'),
               ('Sergipe', 'SE'),
               ('Tocantins', 'TO'),
               ('Distrito Federal', 'DF')
               )

    nome = models.CharField('Name', max_length=20, null=False)
    cpf = models.CharField('CPF', max_length=11, null=False)
    crm = models.CharField('CRM', max_length=6, null=False)
    uf_crm = models.CharField('UF', max_length=25, choices=estados, null=False)
    espec = models.CharField('Expertise', max_length=255, null=False)
    estado = models.CharField('State', max_length=30, choices=estados, null=False)
    cidade = models.CharField('City', max_length=30, null=False)
    numero_fixo = models.CharField('Telephone', max_length=10, default=None)
    whatsapp = models.CharField('Whatsapp', max_length=13, default=None)

    def __str__(self):
        return self.nome


# class Clinic(models.Model):