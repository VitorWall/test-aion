from django.db import models

# Create your models here.


class Produto (models.Model):
    nome = models.CharField(max_length=255, unique=True)
    categoria = models.CharField(max_length=255)

    def __str__ (self):
        return self.nome


class Produto_posicao (models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    posicao = models.CharField(max_length=31)
    quantidade = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.produto.nome + ' - ' + self.posicao


class Pedido_item (models.Model):
    STATUS_CHOICES = [
        ('0', 'A separar'),
        ('1', 'Separado'),
        ('2', 'Em Falta')
    ]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    endereco_destino = models.CharField(max_length=1023)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return str(self.id) + ' - ' + self.produto.nome
