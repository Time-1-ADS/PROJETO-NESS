# Generated by Django 3.2.6 on 2021-11-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211120_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='medic',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='E-mail'),
        ),
    ]