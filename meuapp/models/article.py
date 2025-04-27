from meuapp.models.base import basemodel
from django.db import models
from meuapp.models.reporter import Reporter
class Article(basemodel):
    title=models.CharField(max_length=100,verbose_name='Título do artigo',help_text="Insira o título do artigo")
    pub_date=models.DateTimeField(verbose_name='Data de publicação',help_text="Insira a data de publicação")
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE) #Se o reporter for deletado, todos os artigos do mesmo são removidos juntos
    class Meta:
        abstract=False
    def __str__(self):
        return self.title