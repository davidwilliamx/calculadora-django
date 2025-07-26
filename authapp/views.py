from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('calculator')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calculator')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'authapp/logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('calculator')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authapp/register.html', {'form': form})


"""
Este código Python é um conjunto de views Django que gerenciam a autenticação e registro de usuários para uma aplicação web.

*   **Importações:**
    *   `render`, `redirect`: Funções utilitárias do Django para renderizar templates HTML e redirecionar o navegador para outras URLs, respectivamente.
    *   `authenticate`, `login`, `logout`: Funções do sistema de autenticação do Django para verificar credenciais, iniciar uma sessão de usuário e encerrar uma sessão, respectivamente.
    *   `AuthenticationForm`: Uma classe de formulário integrada do Django para lidar com a entrada de credenciais de login (nome de usuário e senha).
    *   `messages`: Um framework do Django para exibir mensagens (sucesso, erro, aviso) para o usuário em requisições subsequentes.
    *   `RegisterForm`: Um formulário personalizado (presumivelmente definido em `forms.py` dentro do mesmo aplicativo) usado para coletar informações de registro de novos usuários.

*   **`login_view(request)`:**
    *   Esta função de view lida com a lógica de login do usuário.
    *   Primeiro, verifica se o usuário já está autenticado (`request.user.is_authenticated`). Se sim, ele é redirecionado para a URL nomeada 'calculator', evitando que um usuário já logado acesse a página de login novamente.
    *   Se a requisição for um `POST` (ou seja, o formulário de login foi submetido):
        *   Uma instância de `AuthenticationForm` é criada com os dados da requisição.
        *   Se o formulário for válido (as credenciais correspondem a um usuário existente):
            *   O objeto `user` é recuperado do formulário.
            *   A função `login(request, user)` é chamada para iniciar a sessão do usuário.
            *   O usuário é redirecionado para a URL 'calculator'.
        *   Se o formulário não for válido (credenciais incorretas):
            *   Uma mensagem de erro é adicionada (`messages.error`) informando que o usuário ou senha são inválidos.
    *   Se a requisição for um `GET` (ou o `POST` foi inválido e a mensagem de erro foi exibida):
        *   Uma nova instância vazia de `AuthenticationForm` é criada para exibir o formulário.
    *   Finalmente, a view renderiza o template `authapp/login.html`, passando a instância do formulário para exibição.

*   **`logout_view(request)`:**
    *   Esta função de view lida com a saída (logout) do usuário.
    *   Simplesmente chama a função `logout(request)` do Django, que encerra a sessão do usuário atual.
    *   Em seguida, renderiza o template `authapp/logout.html`, que geralmente exibe uma mensagem de confirmação de logout.

*   **`register_view(request)`:**
    *   Esta função de view lida com o registro de novos usuários.
    *   Assim como na `login_view`, verifica se o usuário já está autenticado e o redireciona para 'calculator' se for o caso.
    *   Se a requisição for um `POST` (o formulário de registro foi submetido):
        *   Uma instância de `RegisterForm` (o formulário personalizado de registro) é criada com os dados da requisição.
        *   Se o formulário for válido (todos os campos preenchidos corretamente, senhas correspondendo, etc.):
            *   `form.save(commit=False)` cria uma instância do modelo de usuário, mas não a salva imediatamente no banco de dados. Isso é feito para que a senha possa ser definida com hash antes de salvar.
            *   `user.set_password(form.cleaned_data['password'])` define a senha do usuário de forma segura, aplicando hash.
            *   `user.save()` salva o objeto do usuário (com a senha já com hash) no banco de dados.
            *   Uma mensagem de sucesso é adicionada (`messages.success`) informando que o cadastro foi realizado com sucesso e solicitando o login.
            *   O usuário é redirecionado para a URL nomeada 'login'.
    *   Se a requisição for um `GET` (ou o `POST` foi inválido):
        *   Uma nova instância vazia de `RegisterForm` é criada.
    *   Finalmente, a view renderiza o template `authapp/register.html`, passando a instância do formulário para exibição.

"""
