from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('limpar/', views.limpar_historico, name='limpar_historico'),
]


"""
Este código Python define as rotas (URLs) para uma aplicação Django.

- `from django.urls import path`: Importa a função `path` do módulo `django.urls`, que é usada para definir padrões de URL.
- `from . import views`: Importa o módulo `views` do diretório atual. Este módulo provavelmente contém as funções Python que lidam com as requisições HTTP para as URLs definidas.
- `urlpatterns = [...]`: Esta é uma lista que contém todos os padrões de URL para a aplicação.
    - `path('', views.calculator_view, name='calculator')`: Define uma URL para a raiz da aplicação (o caminho vazio `''`). Quando um usuário acessa a URL base (ex: `http://localhost:8000/`), a função `calculator_view` (definida em `views.py`) será executada. O `name='calculator'` atribui um nome a esta URL, o que permite referenciá-la facilmente em outras partes do projeto Django (como em templates ou redirecionamentos) sem precisar codificar o caminho da URL diretamente.
    - `path('limpar/', views.limpar_historico, name='limpar_historico')`: Define uma URL para o caminho `/limpar/`. Quando um usuário acessa `http://localhost:8000/limpar/`, a função `limpar_historico` (também definida em `views.py`) será executada. Similarmente, `name='limpar_historico'` fornece um nome para esta URL.

"""
