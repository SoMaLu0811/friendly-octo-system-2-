from meuapp.models.base import basemodel
from django.db import models
from meuapp.models.reporter import Reporter
from meuapp.models.magazine import Magazine
class Article(basemodel):
    title=models.CharField(max_length=100,verbose_name='Título do artigo',help_text="Insira o título do artigo")
    pub_date=models.DateTimeField(verbose_name='Data de publicação',help_text="Insira a data de publicação")
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE,verbose_name='Reporter',help_text='Selecione o repórter') #Se o reporter for deletado, todos os artigos do mesmo são removidos juntos
    magazine=models.ManyToManyField(Magazine, verbose_name='Revistas',help_text='Selecione as revistas')
    class Meta:
        abstract=False
    def __str__(self):
        return self.title