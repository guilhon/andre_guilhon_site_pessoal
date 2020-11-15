from django.db import models

class loja_categoria(models.Model):
	cat_nome = models.CharField(max_length=13, verbose_name='Categoria')
	cat_slug = models.SlugField(max_length=100, verbose_name='Identificador')
	cat_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
	cat_modificacao = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

	def __str__(self):
		return self.cat_nome

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['cat_nome']

class loja_produtos(models.Model):
	prod_nome = models.CharField(max_length=13, verbose_name='Produto')
	prod_slug = models.SlugField(max_length=100, verbose_name='Identificador')
	prod_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
	prod_modificacao = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
	prod_categoria = models.ForeignKey(loja_categoria, on_delete=models.DO_NOTHING)
	prod_descricao = models.TextField(max_length=500, verbose_name='Descrição', blank=True)
	prod_valor = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')

	def __str__(self):
		return self.prod_nome

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['prod_nome']


