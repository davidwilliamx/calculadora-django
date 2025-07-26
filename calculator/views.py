from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao
from asteval import Interpreter

aeval = Interpreter()


@login_required(login_url='login')
def calculator_view(request):
    historico = Operacao.objects.filter(usuario=request.user).order_by('-dt_inclusao')[
        :10
    ]
    resultado = ''
    expressao = ''
    if request.method == 'POST':
        expressao = request.POST.get('expressao', '').strip()
        if expressao:
            try:
                expressao_limpa = ''.join(
                    c for c in expressao if c in '0123456789+-*/.() '
                )
                resultado = str(aeval(expressao_limpa))
                if resultado == 'None':
                    resultado = 'Erro'
                else:
                    Operacao.objects.create(
                        usuario=request.user, parametros=expressao, resultado=resultado
                    )
            except Exception:
                resultado = 'Erro'
            request.session['last_result'] = resultado
            return redirect('calculator')
    resultado = request.session.pop('last_result', '')
    return render(
        request,
        'calculator/calculator.html',
        {
            'historico': historico,
            'resultado': resultado,
        },
    )


@login_required(login_url='login')
def limpar_historico(request):
    if request.method == 'POST':
        Operacao.objects.filter(usuario=request.user).delete()
    return redirect('calculator')


"""
Este código Python, escrito no framework Django, define duas views (funções que lidam com requisições web) para uma aplicação de calculadora.

1.  **Importações Iniciais**:
    *   `from django.shortcuts import render, redirect`: Importa funções para renderizar templates HTML e redirecionar requisições.
    *   `from django.contrib.auth.decorators import login_required`: Importa um decorador que garante que um usuário esteja logado para acessar a view.
    *   `from .models import Operacao`: Importa o modelo `Operacao` do mesmo diretório, que provavelmente representa uma operação matemática realizada pelo usuário.
    *   `from asteval import Interpreter`: Importa a classe `Interpreter` da biblioteca `asteval`, que é usada para avaliar expressões matemáticas de forma segura.

2.  **Instância do Interpretador**:
    *   `aeval = Interpreter()`: Cria uma instância do interpretador `asteval`, que será usada para calcular as expressões.

3.  **`calculator_view(request)`**:
    *   `@login_required(login_url='login')`: Este decorador assegura que apenas usuários autenticados possam acessar esta view. Se um usuário não estiver logado, ele será redirecionado para a URL nomeada 'login'.
    *   `historico = Operacao.objects.filter(usuario=request.user).order_by('-dt_inclusao')[:10]`: Recupera as últimas 10 operações (`Operacao`) realizadas pelo usuário atualmente logado, ordenadas da mais recente para a mais antiga.
    *   `resultado = ''` e `expressao = ''`: Inicializam variáveis para armazenar o resultado do cálculo e a expressão digitada.
    *   `if request.method == 'POST'`: Verifica se a requisição HTTP é do tipo POST (geralmente enviada por um formulário).
        *   `expressao = request.POST.get('expressao', '').strip()`: Obtém o valor do campo 'expressao' do formulário POST.
        *   `if expressao:`: Verifica se a expressão não está vazia.
            *   `expressao_limpa = ''.join(c for c in expressao if c in '0123456789+-*/.() ')`: Filtra a expressão para permitir apenas dígitos, operadores matemáticos (`+`, `-`, `*`, `/`), ponto (`.`), parênteses e espaços. Isso é uma medida de segurança para evitar a execução de código malicioso.
            *   `try...except Exception`: Bloco para tratar possíveis erros durante a avaliação da expressão.
                *   `resultado = str(aeval(expressao_limpa))`: Usa o interpretador `aeval` para calcular o resultado da `expressao_limpa`. O resultado é convertido para string.
                *   `if resultado == 'None': resultado = 'Erro'`: Se `asteval` retornar `None` (o que pode acontecer para algumas expressões inválidas), o resultado é definido como 'Erro'.
                *   `else: Operacao.objects.create(...)`: Se o cálculo for bem-sucedido, uma nova entrada `Operacao` é criada no banco de dados, registrando o usuário, a expressão original (`parametros`) e o `resultado`.
            *   `except Exception: resultado = 'Erro'`: Se qualquer erro ocorrer durante a avaliação (ex: divisão por zero, sintaxe inválida), o `resultado` é definido como 'Erro'.
            *   `request.session['last_result'] = resultado`: Armazena o resultado na sessão do usuário. Isso é útil para exibir o resultado após um redirecionamento.
            *   `return redirect('calculator')`: Redireciona o usuário de volta para a mesma view ('calculator'), o que ajuda a prevenir o reenvio do formulário ao atualizar a página e permite exibir o resultado da sessão.
    *   `resultado = request.session.pop('last_result', '')`: Após o redirecionamento (ou em uma requisição GET inicial), recupera o último resultado da sessão e o remove da sessão.
    *   `return render(...)`: Renderiza o template `calculator/calculator.html`, passando o `historico` das operações e o `resultado` atual para serem exibidos na página.

4.  **`limpar_historico(request)`**:
    *   `@login_required(login_url='login')`: Assim como a view da calculadora, esta view também exige que o usuário esteja logado.
    *   `if request.method == 'POST'`: Verifica se a requisição é do tipo POST.
        *   `Operacao.objects.filter(usuario=request.user).delete()`: Se for POST, todas as operações (`Operacao`) associadas ao usuário logado são removidas do banco de dados.
    *   `return redirect('calculator')`: Redireciona o usuário de volta para a view da calculadora após a limpeza do histórico.



"""
