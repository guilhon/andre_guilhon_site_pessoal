from django.db import models

TIPO_DE_PLANETA = [
	('Indeterminado','Indeterminado'),
    ('Rochoso','Rochoso'),
    ('Gasoso','Gasoso'),
]

class planetas(models.Model):
	planeta = models.CharField(max_length=30)
	tipo = models.CharField(max_length=13, choices=TIPO_DE_PLANETA)
	massa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	data_mod = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.planeta


