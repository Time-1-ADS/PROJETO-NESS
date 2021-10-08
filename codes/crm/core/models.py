from django.db import models
from django.urls import reverse


class Agent(models.Model):

    nome = models.CharField('Nome', max_length=20, null=False)
    email = models.EmailField('E-mail', null=False)
    senha = models.CharField('Senha', max_length=255, null=False)
    cargo = models.ForeignKey('Permission', on_delete=models.CASCADE)
    foto = models.ImageField('Foto', upload_to='static/img', null=True)

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
    cargo = models.CharField('Cargo', max_length=13, choices=cargo_choices, default=sales)

    def __str__(self):
        return self.cargo


class Medic(models.Model):
    estados = (('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'),
               ('Bahia', 'BA'), ('Ceará', 'CE'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'),
               ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'),
               ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'),
               ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'),
               ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'),
               ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'),
               ('Sergipe', 'SE'), ('Tocantins', 'TO'), ('Distrito Federal', 'DF'))

    produtos_medic = (('nReport', 'nR'), ('Iara', 'Iara'))  # 'nMonitor', 'nSensor', 'nCommand', 'nEcho',

    nome = models.CharField('Nome', max_length=20, null=False)
    cpf = models.CharField('CPF', max_length=11, null=False)
    crm = models.CharField('CRM', max_length=6, null=False)
    uf_crm = models.CharField('UF', max_length=25, choices=estados, null=False)
    espec = models.CharField('Especialidade', max_length=255, null=False)
    estado = models.CharField('Estado', max_length=30, choices=estados, null=False)
    cidade = models.CharField('Cidade', max_length=30, null=False)
    numero_fixo = models.CharField('Telefone', max_length=10, default=None)
    whatsapp = models.CharField('Whatsapp', max_length=13, default=None)
    produto = models.CharField('Produto', max_length=255, choices=produtos_medic, null=False)

    def __str__(self):
        return self.nome


class Clinic(models.Model):
    categoria = (('Clinica', 'Clinica'), ('Hospital', 'Hospital'), ('Laboratório', 'Laboratório'),
                 ('Agência de plano de Saúde', 'Agência de plano de Saúde'))
    produtos = (('nMonitor', 'nMonitor'), ('nSensor', 'nSensor'), ('nCommand', 'nCommand'), ('nEcho', 'nEcho'),
                ('nReport', 'nR'), ('Iara', 'Iara'))

    categoria = models.CharField('Categoria', max_length=100, choices=categoria, null=False)
    razao = models.CharField('Razão Social', max_length=255, null=False)
    cnpj = models.CharField('CNPJ', max_length=14, null=False)
    numero = models.CharField('Número', max_length=100, null=False)
    email = models.EmailField('E-mail', max_length=100, null=False)
    produto = models.CharField('Produto', max_length=100, choices=produtos, null=False)

    def __str__(self):
        return self.razao


class Empresa(models.Model):
    medico = models.ForeignKey('Medic', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Clinic', on_delete=models.CASCADE)
    tudo = [medico, empresa]

    def __str__(self):
        return self.tudo


class Pipeline(models.Model):
    status_projeto = (('Novo', 'Novo'), ('Aberto', 'Aberto'), ('Pendente', 'Pendente'), ('Fechado', 'Fechado'))

    nome = models.CharField('Nome do Projeto', max_length=255, null=False)
    empresa = models.CharField('Empresa', max_length=255, null=False)
    valor_total = models.DecimalField('Valor total', max_digits=30, decimal_places=0, null=False)
    status = models.CharField('Status', max_length=255, choices=status_projeto, default='Novo', null=False)
    descricao = models.TextField('Descrição', max_length=500, null=False)
    data_ini = models.DateField('Data', null=False)
    visivel = models.ForeignKey('Permission', on_delete=models.CASCADE)
