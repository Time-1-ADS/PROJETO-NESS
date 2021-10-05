from django.db import models
from django.urls import reverse


class Agent(models.Model):

    nome = models.CharField('Name', max_length=20, help_text='Enter the name of Agent.', null=False)
    email = models.EmailField('E-mail', help_text='Enter the Agent email address.', null=False)
    senha = models.CharField('Password', max_length=255, null=False)
    cargo = models.ForeignKey('Permission', on_delete=models.CASCADE)
    foto = models.ImageField('Image', upload_to='static/img', null=True)

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

    nome = models.CharField('Name', max_length=20, help_text='Enter the name of Medic.', null=False)
    cpf = models.CharField('CPF', max_length=11, help_text='Enter only numbers.', null=False)
    crm = models.CharField('CRM', max_length=6, help_text='Enter your 6 crm numbers.', null=False)
    uf_crm = models.CharField('UF', max_length=25, choices=estados, null=False)
    espec = models.CharField('Expertise', max_length=255, null=False)
    estado = models.CharField('State', max_length=30, choices=estados, help_text='Enter which state you live in',
                              null=False)
    cidade = models.CharField('City', max_length=30, help_text='Enter which City you live in', null=False)
    numero_fixo = models.CharField('Telephone', max_length=10, help_text='Enter your number like: 0000000000, put your DDD',
                                   default=None)
    whatsapp = models.CharField('Whatsapp', max_length=13, help_text='Enter your number like: 0000000000, put your DDD and DDI',
                                   default=None)

    def __str__(self):
        return self.nome


# class Clinic(models.Model):