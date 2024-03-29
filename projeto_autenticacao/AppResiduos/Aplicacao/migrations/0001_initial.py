# Generated by Django 2.2.5 on 2019-10-24 16:48

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
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
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
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
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Carteira')),
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
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('seg', 'segunda-feira'), ('ter', 'terça-feira'), ('qua', 'quarta-feira'), ('qui', 'quinta-feira'), ('sex', 'sexta-feira')], max_length=3)),
                ('horario_coleta', models.TimeField()),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Cliente')),
            ],
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
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacao.Endereco'),
        ),
    ]
