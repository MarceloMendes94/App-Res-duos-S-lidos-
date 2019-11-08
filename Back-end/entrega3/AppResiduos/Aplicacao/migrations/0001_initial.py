# Generated by Django 2.2.7 on 2019-11-08 03:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=30)),
                ('servico', models.CharField(choices=[('Netflix', 'Netflix'), ('Spotify', 'Spotify'), ('Uber', 'Uber')], default=None, max_length=7)),
                ('descricao', models.TextField(default='', max_length=1000)),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(help_text='Informe a sigla do seu estado.\nExemplo: ES (Espírito Santo)', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TrashCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('estado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Estado')),
                ('nome_cidade', models.CharField(help_text='Informe a cidade onde reside.\nExemplo: Serra', max_length=35)),
            ],
            bases=('Aplicacao.estado',),
        ),
        migrations.CreateModel(
            name='InfoAdicional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(help_text='Informe o CPF sem caractéres especiais', max_length=14)),
                ('dt_nascimento', models.DateField(help_text='Informe a sua data de nascimento')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Habilitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14)),
                ('tipo', models.CharField(max_length=5)),
                ('validade', models.DateField()),
                ('motorista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Motorista')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('razao_social', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContaBanco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_conta', models.IntegerField(help_text='Informe o número da conta para depósito de pagamentos.', max_length=32)),
                ('agencia', models.IntegerField(help_text='Informe o número da sua agencia.', max_length=4)),
                ('tipo_conta', models.IntegerField(help_text='Informe o número identificador do tipo de conta.\nExemplo: 500 para poupança.', max_length=3)),
                ('motorista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Motorista')),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_carteira', models.CharField(choices=[('Cliente', 'Cliente'), ('Motorista', 'Motorista')], default=None, max_length=9)),
                ('saldo_real', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('saldo_trashcoin', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('cidade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Cidade')),
                ('nome_bairro', models.CharField(help_text='Informe o bairro onde reside.\nExemplo: Manguinhos', max_length=35)),
            ],
            bases=('Aplicacao.cidade',),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('bairro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Aplicacao.Bairro')),
                ('logradouro', models.CharField(help_text='Exemplo: Alameda, área, avenida, campo, chácara', max_length=30)),
                ('cep', models.CharField(help_text='Informe o CEP sem caractéres especiais', max_length=8)),
                ('numero', models.CharField(help_text='Número da residência ou local', max_length=4)),
                ('referencia', models.CharField(help_text='Exemplo: Prédio João Maria, apartamento 201', max_length=50)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Cliente')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Empresa')),
                ('motorista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Motorista')),
            ],
            bases=('Aplicacao.bairro',),
        ),
    ]
