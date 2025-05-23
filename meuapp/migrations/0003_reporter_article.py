# Generated by Django 5.2 on 2025-04-27 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0002_person_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insira seu nome completo', max_length=100, verbose_name='Nome Completo')),
                ('email', models.EmailField(help_text='Insira seu E-mail', max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(help_text='Insira seu número de cpf', max_length=11, verbose_name='CPF')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Insira o título do artigo', max_length=100, verbose_name='Título do artigo')),
                ('pub_date', models.DateTimeField(help_text='Insira a data de publicação', verbose_name='Data de publicação')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.reporter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
