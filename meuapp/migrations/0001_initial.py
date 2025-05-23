# Generated by Django 5.2 on 2025-04-27 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Descriça da sua conta', max_length=200)),
                ('number', models.CharField(help_text='Insira o número da sua conta', max_length=200)),
                ('balance', models.FloatField(default=0, help_text='Insira o seu saldo inicial')),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Conta')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
