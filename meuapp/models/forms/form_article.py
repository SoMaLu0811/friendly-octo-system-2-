#Formulário de submissão de artigos
from django.forms import ModelForm
from meuapp.models.article import Article
class ArticileForm(ModelForm):
    #Formulário será salvo no banco de dados
    class Meta:
        model=Article
        fields='__all__'
        exclude=['pub_date']
        
