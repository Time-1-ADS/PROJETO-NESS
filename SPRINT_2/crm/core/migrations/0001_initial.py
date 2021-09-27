# Generated by Django 3.2.6 on 2021-09-25 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(choices=[('ADM', 'Administrador'), ('DIRETOR', 'Diretor'), ('AGENT', 'Agente')], default='AGENT', max_length=7, verbose_name='Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Type the name of Agent.', max_length=20, verbose_name='Name')),
                ('email', models.EmailField(help_text='Type the Agent email address.', max_length=254, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=255, verbose_name='Password')),
                ('foto', models.ImageField(height_field=32, upload_to='static/img', verbose_name='Image', width_field=32)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.permission')),
            ],
        ),
    ]
