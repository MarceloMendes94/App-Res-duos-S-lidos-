# Generated by Django 2.2.5 on 2019-10-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente_nome_completo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tefefone',
            field=models.CharField(default="None", max_length=11),
            preserve_default=False,
        ),
    ]