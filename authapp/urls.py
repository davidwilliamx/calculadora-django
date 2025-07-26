from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

"""
Este código define as rotas (URLs) para uma aplicação Django. Ele mapeia caminhos de URL específicos para funções de visualização (views) correspondentes, que são responsáveis por processar as requisições para esses caminhos.

- `from django.urls import path`: Importa a função `path` do módulo `django.urls`, que é usada para definir padrões de URL.
- `from . import views`: Importa o módulo `views` do diretório atual. Este módulo provavelmente contém as funções que lidam com a lógica para cada URL.
- `urlpatterns = [...]`: Esta é uma lista Python onde cada elemento é uma definição de URL.
    - `path('login/', views.login_view, name='login')`: Define uma rota para o caminho `/login/`. Quando um usuário acessa `exemplo.com/login/`, a função `login_view` (definida no módulo `views`) será executada. O `name='login'` fornece um nome para esta URL, permitindo que ela seja referenciada em outras partes do código Django (por exemplo, em templates ou redirecionamentos) de forma independente do caminho real.
    - `path('logout/', views.logout_view, name='logout')`: Similarmente, define uma rota para `/logout/` que chama a função `logout_view`.
    - `path('register/', views.register_view, name='register')`: Define uma rota para `/register/` que chama a função `register_view`.

Em resumo, este arquivo configura as URLs para funcionalidades de autenticação e registro de usuários em uma aplicação Django.
"""
