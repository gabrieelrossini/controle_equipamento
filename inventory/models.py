from django.db import models


class Sala(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    nome = models.CharField(max_length=140)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name="equipamentos")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="equipamentos")
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
