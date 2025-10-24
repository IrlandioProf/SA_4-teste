from django.urls import path
from page_app.views import index, contato

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),

    path('contato/', contato),
]