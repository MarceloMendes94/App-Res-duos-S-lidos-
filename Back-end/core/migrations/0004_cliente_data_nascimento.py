# Generated by Django 2.2.5 on 2019-10-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_tefefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(default=None, null=True),
            preserve_default=False,
        ),
    ]