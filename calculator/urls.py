from django.urls import (
    path,
)  # Importa a função 'path' do módulo 'urls' do Django, essencial para definir rotas de URL.
from . import (
    views,
)  # Importa o módulo 'views' do diretório atual, onde as funções de visualização da sua calculadora estão definidas.

# Lista que armazena todas as configurações de URL para este aplicativo da calculadora.
urlpatterns = [
    # Define a URL raiz da aplicação da calculadora.
    # O caminho vazio '' significa que esta URL corresponde à raiz (ex: /calculadora/).
    # views.calculator_view é a função de visualização que renderiza a página principal da calculadora.
    # name='calculator' é um nome de atalho para esta URL, útil para referenciá-la em templates e código Python.
    path('', views.calculator_view, name='calculator'),
    # Define a URL para limpar o histórico de operações.
    # 'limpar/' é o caminho da URL para acionar essa funcionalidade.
    # views.limpar_historico é a função de visualização que executa a limpeza do histórico.
    # name='limpar_historico' é o nome de atalho para esta URL.
    path('limpar/', views.limpar_historico, name='limpar_historico'),
]
