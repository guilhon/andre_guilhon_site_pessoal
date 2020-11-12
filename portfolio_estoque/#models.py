from django.db import models

TIPO_DE_PLANETA = [
	('Indeterminado','Indeterminado'),
    ('Rochoso','Rochoso'),
    ('Gasoso','Gasoso'),
]

class estoque(models.Model):
	produto = models.CharField(max_length=30)
	quantidade = models.CharField(max_length=13, choices=TIPO_DE_PLANETA)
	valor = models.FloatField(max_length=30, null=True, blank=True)
	data_mod = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.produto

class historico(models.Model):
	produto_vendido = models.CharField(max_length=30)
	quantidade_vendida = models.CharField(max_length=13, choices=TIPO_DE_PLANETA)
	valor_total = models.FloatField(max_length=30, null=True, blank=True)
	data_venda = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.produto_vendido
