from django.shortcuts import render, get_object_or_404, redirect
from .models import planetas
from .forms import planetasForm
from django.contrib import messages
from django.db.models import Q # Utilizado para o sistema de busca
from django.core.paginator import Paginator # Paginação
from datetime import date

def listar_planetas(request):
	lista_dos_planetas = planetas.objects.all()
	valor_busca = request.GET.get('q') # Utilizado para o sistema de busca
	if valor_busca: # Se existe algum valor de busca vamos redefinir nossa variável de lista_dos_planetas
		lista_dos_planetas = planetas.objects.filter(
				Q(planeta__icontains=valor_busca)|
				Q(tipo__icontains=valor_busca)|
				Q(massa__icontains=valor_busca)
			)
	paginator = Paginator(lista_dos_planetas, 10)
	page_number = request.GET.get('page')
	lista_dos_planetas = paginator.get_page(page_number)
	return render(request, 'portfolio_CRUD.html', {'lista_dos_planetas':lista_dos_planetas})

def adicionar_planeta(request):
	if request.method == 'POST':
		formulario = planetasForm(request.POST or None)
		if formulario.is_valid():
			formulario.save()
			formulario = planetasForm()
			messages.success(request, 'Planeta adicionado com sucesso.')
			return redirect('listar_planetas')
	else:
		formulario = planetasForm()
	return render(request, 'portfolio_CRUD/adicionar_planeta.html', {'formulario':formulario})

def editar_planeta(request, id):
	planeta_escolhido = get_object_or_404(planetas, id=id)
	formulario = planetasForm(request.POST or None, instance=planeta_escolhido)
	if formulario.is_valid():
		formulario.save()
		formulario = planetasForm()
		messages.success(request, 'Planeta alterado com sucesso.')
		return redirect('listar_planetas')
	return render(request, 'portfolio_CRUD/editar_planeta.html', {'formulario':formulario})

def ver_planeta(request, id):
	planeta_escolhido = get_object_or_404(planetas, id=id)
	return render(request, 'portfolio_CRUD/ver_planeta.html', {'planeta_escolhido':planeta_escolhido})

def excluir_planeta(request,id):
	planeta_escolhido = get_object_or_404(planetas, id=id)
	if request.method == 'POST':
		planeta_escolhido.delete()
		messages.warning(request, 'Planeta excluído com sucesso.')
		return redirect('listar_planetas')
	return render(request, "portfolio_CRUD/excluir_planeta.html", {'planeta_escolhido': planeta_escolhido})

def inserir_planetas(request):

	lista = [['Mercúrio','Rochoso',0.1], 
			['Vênus','Rochoso',0.8],
			['Terra','Rochoso',1],
			['Marte','Rochoso',0.1],
			['Júpiter','Gasoso',318],
			['Saturno','Gasoso',95],
			['Urano','Gasoso',14],
			['Netuno','Gasoso',17],
	]

	for i in range(8):
		existe_planeta = planetas.objects.filter(planeta=lista[i][0])
		if existe_planeta:
			planetas.objects.filter(planeta=lista[i][0]).delete()
			planetas.objects.create(planeta=lista[i][0], tipo=lista[i][1], massa=lista[i][2])
		else:
			planetas.objects.create(planeta=lista[i][0], tipo=lista[i][1], massa=lista[i][2])

	messages.success(request, 'Todos os planetas do Sistema Solar estão atualizados na lista!')
	return redirect('listar_planetas')