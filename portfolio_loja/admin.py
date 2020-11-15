from django.contrib import admin
from .models import loja_categoria, loja_produtos

class loja_categoriaAdmin(admin.ModelAdmin):

	list_display = ['cat_nome', 'cat_slug', 'cat_criacao', 'cat_modificacao']

class loja_produtosAdmin(admin.ModelAdmin):
	
	list_display = ['prod_nome', 'prod_slug', 'prod_criacao', 'prod_modificacao', 'prod_categoria', 'prod_descricao', 'prod_valor' ]

admin.site.register(loja_categoria, loja_categoriaAdmin)
admin.site.register(loja_produtos, loja_produtosAdmin)
