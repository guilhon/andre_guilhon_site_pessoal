from django.contrib import admin
from .models import loja_categoria, loja_produtos

#class loja_produtosAdmin(admin.ModelAdmin):
#	list_display = ['prod_nome', 'prod_slug', 'prod_criacao', 'prod_modificacao', 'prod_descricao', 'prod_valor' ]


admin.site.register(loja_categoria)
admin.site.register(loja_produtos)
#admin.site.register(loja_produtos, loja_produtosAdmin)