# Generated by Django 3.2.6 on 2021-11-06 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pipeline_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipeline',
            name='clinica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.clinic'),
        ),
        migrations.AddField(
            model_name='pipeline',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.medic'),
        ),
    ]
