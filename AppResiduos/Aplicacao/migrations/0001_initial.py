# Generated by Django 2.1 on 2019-11-10 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Carteira')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aguardando', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('razao_social', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaCupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('imagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilitacao', models.CharField(max_length=11)),
                ('placa', models.CharField(max_length=7)),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Carteira')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pesagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Residuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_residuo', models.CharField(max_length=35)),
                ('valor_kilo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('estado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Estado')),
                ('nome_cidade', models.CharField(max_length=35)),
            ],
            bases=('Aplicacao.estado',),
        ),
        migrations.AddField(
            model_name='pesagem',
            name='Residuo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Residuo'),
        ),
        migrations.AddField(
            model_name='pesagem',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Cliente'),
        ),
        migrations.AddField(
            model_name='pesagem',
            name='motorista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Motorista'),
        ),
        migrations.AddField(
            model_name='cupom',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.EmpresaCupom'),
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('cidade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Cidade')),
                ('nome_bairro', models.CharField(max_length=35)),
            ],
            bases=('Aplicacao.cidade',),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('bairro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Bairro')),
                ('logradouro', models.TextField()),
                ('cep', models.CharField(max_length=8)),
                ('numero', models.CharField(max_length=4)),
                ('referencia', models.TextField()),
            ],
            bases=('Aplicacao.bairro',),
        ),
        migrations.AddField(
            model_name='motorista',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Endereco'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Endereco'),
        ),
    ]
