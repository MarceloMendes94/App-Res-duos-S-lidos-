# Generated by Django 2.2.5 on 2019-11-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacao', '0002_auto_20191110_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(help_text='Informe sua data de nascimento ex: AAAA-MM-DD'),
        ),
    ]
