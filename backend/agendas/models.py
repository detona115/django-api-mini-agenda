from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Agenda(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Data',)
    person = models.CharField('Pessoa', max_length=100)
    subject = models.CharField('Assunto', max_length=100)
    PRIORIDADE = [
        ('alta', 'ALTA'),
        ('media', 'MEDIA'),
        ('baixa', 'BAIXA'),
    ]
    priority = models.CharField('Prioridade', max_length=5, choices=PRIORIDADE)
    place = models.CharField('Local', max_length=100)
    email = models.EmailField('E-mail',)
    contact = models.CharField('Telefone', max_length=20)

    class Meta:
        indexes = [models.Index(fields=['date'])]
        ordering = ['date']

    def __str__(self):
        return self.subject