# Generated by Django 5.2 on 2025-04-27 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insira seu nome', max_length=100, verbose_name='Nome')),
                ('birth_date', models.DateField(help_text='Insira sua data de nascimento', verbose_name='data de nascimento')),
                ('cpf', models.CharField(help_text='Insira seu CPF', max_length=11, verbose_name='cpf')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('number', models.CharField(help_text='Insira seu número de passaporte', max_length=10, verbose_name='passaporte')),
                ('issue_date', models.DateField(help_text='Insira sua data de expedição', verbose_name='Issue_date')),
                ('expiration_date', models.DateField(help_text='Insira a sua data de validade do seu passaporte', verbose_name='Data de validade')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='meuapp.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
