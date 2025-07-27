from django.shortcuts import (
    render,
    redirect,
)  # Importa funções para renderizar templates HTML e redirecionar para outras URLs.
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)  # Funções do Django para autenticar, logar e deslogar usuários.
from django.contrib.auth.forms import (
    AuthenticationForm,
)  # Formulário padrão do Django para autenticação de usuário (login).
from django.contrib import (
    messages,
)  # Módulo para exibir mensagens de notificação (sucesso, erro, etc.) para o usuário.
from .forms import (
    RegisterForm,
)  # Importa o formulário de registro personalizado que você criou no arquivo 'forms.py'.


def login_view(request):
    """
    Função de visualização para lidar com o login de usuários.
    Se o usuário já estiver autenticado, ele é redirecionado para a página da calculadora.
    Processa o formulário de login e autentica o usuário.
    """
    # Se o usuário já estiver logado, redireciona para a página da calculadora.
    if request.user.is_authenticated:
        return redirect('calculator')

    # Verifica se a requisição é um POST (envio do formulário de login).
    if request.method == 'POST':
        # Instancia o formulário de autenticação com os dados da requisição.
        form = AuthenticationForm(request, data=request.POST)
        # Verifica se o formulário é válido (usuário e senha corretos).
        if form.is_valid():
            # Obtém o objeto de usuário autenticado.
            user = form.get_user()
            # Realiza o login do usuário na sessão.
            login(request, user)
            # Redireciona o usuário para a página da calculadora após o login bem-sucedido.
            return redirect('calculator')
        else:
            # Se o formulário for inválido, adiciona uma mensagem de erro.
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        # Se a requisição não for POST (primeira vez acessando a página), cria um formulário vazio.
        form = AuthenticationForm()

    # Renderiza o template de login, passando o formulário para exibição.
    return render(request, 'authapp/login.html', {'form': form})


def logout_view(request):
    """
    Função de visualização para lidar com o logout de usuários.
    Desloga o usuário da sessão.
    """
    # Desloga o usuário atualmente autenticado.
    logout(request)
    # Renderiza o template da página de logout (pode ser uma confirmação ou redirecionamento).
    return render(request, 'authapp/logout.html')


def register_view(request):
    """
    Função de visualização para lidar com o registro de novos usuários.
    Se o usuário já estiver autenticado, ele é redirecionado para a página da calculadora.
    Processa o formulário de registro, cria e salva o novo usuário.
    """
    # Se o usuário já estiver logado, redireciona para a página da calculadora.
    if request.user.is_authenticated:
        return redirect('calculator')

    # Verifica se a requisição é um POST (envio do formulário de registro).
    if request.method == 'POST':
        # Instancia o formulário de registro com os dados da requisição.
        form = RegisterForm(request.POST)
        # Verifica se o formulário é válido (campos preenchidos corretamente e senhas coincidem).
        if form.is_valid():
            # Salva o usuário do formulário, mas não o persiste no banco de dados ainda.
            # Isso permite definir a senha com hash antes de salvar.
            user = form.save(commit=False)
            # Define a senha do usuário, garantindo que seja armazenada com hash (segurança).
            user.set_password(form.cleaned_data['password'])
            # Salva o objeto de usuário no banco de dados.
            user.save()
            # Adiciona uma mensagem de sucesso para o usuário.
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            # Redireciona para a página de login após o registro bem-sucedido.
            return redirect('login')
    else:
        # Se a requisição não for POST, cria um formulário de registro vazio.
        form = RegisterForm()

    # Renderiza o template de registro, passando o formulário para exibição.
    return render(request, 'authapp/register.html', {'form': form})
