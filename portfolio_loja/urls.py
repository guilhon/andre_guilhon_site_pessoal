from django.urls import path
from .views import (
    loja_principal,
    )

urlpatterns = [
    path('portfolio_loja/', loja_principal, name='loja_principal'),
]
