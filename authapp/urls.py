from django.urls import (
    path,
)  # Importa a função 'path' do módulo 'urls' do Django, usada para definir rotas de URL.
from . import (
    views,
)  # Importa o módulo 'views' do diretório atual (representado por '.'), onde as funções de visualização estão definidas.

# Lista que armazena todas as configurações de URL para este aplicativo.
urlpatterns = [
    # Define a URL para a página de login.
    # 'login/' é o caminho da URL.
    # views.login_view é a função de visualização que será chamada quando esta URL for acessada.
    # name='login' é um nome único para esta URL, útil para referenciá-la em templates ou outras partes do código.
    path('login/', views.login_view, name='login'),
    # Define a URL para a funcionalidade de logout.
    # views.logout_view é a função que lida com o logout do usuário.
    # name='logout' é o nome para referência.
    path('logout/', views.logout_view, name='logout'),
    # Define a URL para a página de registro de novos usuários.
    # views.register_view é a função de visualização responsável por exibir e processar o formulário de registro.
    # name='register' é o nome para referência.
    path('register/', views.register_view, name='register'),
]
