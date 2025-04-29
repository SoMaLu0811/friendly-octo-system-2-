#Modelo de registro de autor de artigos publicados no site
from meuapp.models.base import basemodel
from django.db import models
class Reporter(basemodel):
    name=models.CharField(max_length=100,verbose_name='Nome Completo',help_text="Insira seu nome completo")
    email=models.EmailField(verbose_name='E-mail',help_text="Insira seu E-mail")
    cpf=models.CharField(max_length=11,verbose_name='CPF',help_text="Insira seu número de cpf")
    idade=models.CharField(max_length=3,default=0,verbose_name='Idade',help_text='Digite sua idade:')
    nacionalidade=models.CharField(max_length=100, default='Não especificado',verbose_name='Nacionalidade',help_text='Insira aqui sua nacionalidade')
    
    descrição=models.CharField(max_length=200,default='',help_text='Insira a descrição do escritor')
    
    class Meta:
        abstract=False
    def __str__(self):
        return self.name