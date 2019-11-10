# Generated by Django 2.2.7 on 2019-11-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtHora', models.DateTimeField(help_text='Informe a data e hora da coleta')),
            ],
        ),
        migrations.AddField(
            model_name='motorista',
            name='placa',
            field=models.CharField(default=None, help_text='Informe a placa do seu veiculo', max_length=10),
        ),
    ]