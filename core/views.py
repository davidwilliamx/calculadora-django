from django.shortcuts import (
    redirect,
)  # Importa a função 'redirect' do Django, usada para redirecionar o usuário para outra URL.
from django.contrib.auth.decorators import (
    login_required,
)  # Embora importado, este decorador não é usado diretamente nesta função,

# pois a lógica de redirecionamento já lida com usuários autenticados e não autenticados.


def home_redirect(request):
    """
    Função de visualização para redirecionar o usuário após acessar a URL raiz.
    Verifica se o usuário está autenticado:
    - Se sim, redireciona para a página da calculadora.
    - Se não, redireciona para a página de login.
    """
    # Verifica se o usuário que fez a requisição está autenticado (logado).
    if request.user.is_authenticated:
        # Se estiver autenticado, redireciona para a URL nomeada 'calculator'.
        return redirect('calculator')
    # Se o usuário não estiver autenticado, redireciona para a URL nomeada 'login'.
    return redirect('login')
