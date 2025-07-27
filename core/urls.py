from django.contrib import (
    admin,
)  # Importa o módulo 'admin' do Django, que inclui o painel de administração.
from django.urls import (
    path,
    include,
)  # Importa 'path' para definir URLs individuais e 'include' para incluir URLs de outras apps.
from .views import (
    home_redirect,
)  # Importa a view 'home_redirect' do arquivo views.py do diretório atual.


# Lista principal que define os padrões de URL para todo o projeto Django.
# O Django processa essas URLs em ordem, de cima para baixo.
urlpatterns = [
    # Mapeia a URL raiz do seu site ('').
    # Quando alguém acessa a URL base (ex: http://localhost:8000/), a função 'home_redirect' será chamada.
    # 'name='home'' é um atalho para referenciar esta URL em outras partes do seu código.
    path('', home_redirect, name='home'),
    # Mapeia a URL para o painel de administração do Django.
    # 'admin/' é o caminho para acessar o painel.
    # 'admin.site.urls' inclui todas as URLs padrão fornecidas pelo Django para o painel de administração.
    path('admin/', admin.site.urls),
    # Inclui os padrões de URL do aplicativo 'authapp'.
    # Isso significa que qualquer URL que comece com 'auth/' (ex: /auth/login, /auth/register)
    # será tratada pelas URLs definidas no arquivo 'authapp/urls.py'.
    path('auth/', include('authapp.urls')),
    # Inclui os padrões de URL do aplicativo 'calculator'.
    # Similar ao 'authapp', URLs que começam com 'calculator/' (ex: /calculator/, /calculator/limpar)
    # serão tratadas pelas URLs definidas no arquivo 'calculator/urls.py'.
    path('calculator/', include('calculator.urls')),
]
