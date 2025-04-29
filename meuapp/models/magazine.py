from meuapp.models.base import basemodel
from django.db import models
class Magazine(basemodel):
    name=models.CharField(max_length=100,default='Não especificado',verbose_name='Nome da revista',help_text='Insira o nome da revista')
    edition=models.IntegerField(verbose_name='Edição da Revista',help_text='Insira a edição da Revista')
    class Meta:
        abstract=False
        
    def __str__(self):
        return f'{self.name}: {self.edition}'
    
    
    