from django.shortcuts import render, get_object_or_404, redirect
#from .models import planetas
#from .forms import planetasForm

def loja_principal(request):
	return render(request, 'portfolio_loja/index.html')

