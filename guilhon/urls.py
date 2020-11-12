from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('', include('portfolio_crud.urls')),
]


"""
Também funciona
urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include('principal.urls')),
    path(route='', view=include('portfolio_crud.urls')),
]
"""
