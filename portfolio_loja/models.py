from django.db import models

class loja_categoria(models.Model):
	cat_nome = models.CharField(max_length=13, verbose_name='Categoria')
	cat_slug = models.SlugField(max_length=100)
	cat_criacao = models.DateTimeField(auto_now_add=True)
	cat_modificacao = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.cat_nome

	class Meta:
		verbose_name = 'Loja - Categoria'
		verbose_name_plural = 'Loja - Categorias'
		ordering = ['cat_nome']

class loja_produtos(models.Model):
	prod_nome = models.CharField(max_length=13, verbose_name='Planeta / Produto')
	prod_slug = models.SlugField(max_length=100)
	prod_criacao = models.DateTimeField(auto_now_add=True)
	prod_modificacao = models.DateTimeField(auto_now=True)
	prod_categoria = models.ForeignKey(loja_categoria, on_delete=models.DO_NOTHING)
	prod_descricao = models.TextField(max_length=500, verbose_name='Descrição', blank=True)
	prod_valor = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')

	def __str__(self):
		return self.prod_nome

	class Meta:
		verbose_name = 'Loja - Produto'
		verbose_name_plural = 'Loja - Produtos'
		ordering = ['prod_nome']


