from django.db import models

# Create your models here.

##########################################################################################################################

#CONFIGURAÇÕES DOS CHOICES

##########################################################################################################################

especie = (
    ('Cachorro', 'cachorro'),
    ('Cavalo', 'cavalo'),
    ('Gato', 'gato'),
    ('Periquito', 'periquito')
    
    
)

raca = (
    ('Shih-Tzu', 'Shih-Tzu'),
    ('Buldogue Francês', 'Buldogue Francês'),
    ('Yorkshire Terrier','Yorkshire Terrier'),
    ('Poodle','Poodle'),
    ('Maltês','Maltês'),
    ('Pug','Pug'),
    ('Sem raça definida','SRD')
)

cor = (
    ('Amarelo', 'Amarelo'),
    ('Azul', 'Azul'),
    ('Branco', 'Branco'),
    ('Marrom', 'Marrom'),
    ('Preto', 'Preto')
)

tamanho = (
    ('P', 'pequeno'),
    ('M', 'medio'),
    ('G', 'grande')
)

##########################################################################################################################

class Perdido(models.Model):
    especie = models.CharField(max_length=20, choices = especie)
    raca = models.CharField(max_length=20, choices = raca)
    cor = models.CharField(max_length=20, choices=cor)
    tamanho = models.CharField(max_length=1, choices = tamanho)
    localidade = models.CharField(max_length=20)
    caracteristica = models.CharField(max_length=20)
    tempo = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)

class Encontrado(models.Model):
    especie = models.CharField(max_length=20, choices=especie)
    raca = models.CharField(max_length=20, choices=raca)
    cor = models.CharField(max_length=20, choices=cor)
    tamanho = models.CharField(max_length=1, choices = tamanho)
    localidade = models.CharField(max_length=20)
    caracteristica = models.CharField(max_length=20)
    tempo = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)