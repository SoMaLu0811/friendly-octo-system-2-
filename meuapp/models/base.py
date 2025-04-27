from django.db import models
class basemodel(models.Model):
    class Meta:
        abstract=True
        app_label='meuapp'
        
        