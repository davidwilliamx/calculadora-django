from django.shortcuts import (
    render,
    redirect,
)  # Importa funções para renderizar templates HTML e redirecionar para outras URLs.
from django.contrib.auth.decorators import (
    login_required,
)  # Importa o decorador 'login_required' para restringir o acesso a views apenas para usuários logados.
from .models import (
    Operacao,
)  # Importa o modelo 'Operacao' que você definiu, usado para salvar o histórico de cálculos.
from asteval import (
    Interpreter,
)  # Importa a classe 'Interpreter' da biblioteca 'asteval', que permite avaliar expressões matemáticas como strings.

# Cria uma instância do interpretador 'asteval'.
# Esta instância será usada para calcular o resultado das expressões matemáticas.
aeval = Interpreter()


# Decorador que garante que esta view só pode ser acessada por usuários autenticados.
# Se o usuário não estiver logado, ele será redirecionado para a URL com o nome 'login'.
@login_required(login_url='login')
def calculator_view(request):
    """
    Função de visualização principal para a calculadora.
    Exibe o histórico de operações do usuário e processa novas expressões.
    """
    # Busca as últimas 10 operações do usuário logado, ordenadas pela data de inclusão (mais recentes primeiro).
    historico = Operacao.objects.filter(usuario=request.user).order_by('-dt_inclusao')[
        :10
    ]

    resultado = ''  # Inicializa a variável para o resultado do cálculo.
    expressao = ''  # Inicializa a variável para a expressão recebida.

    # Verifica se a requisição é um POST, o que indica que uma nova expressão foi enviada.
    if request.method == 'POST':
        # Obtém a expressão do corpo da requisição POST e remove espaços em branco extras.
        expressao = request.POST.get('expressao', '').strip()

        # Processa a expressão apenas se ela não estiver vazia.
        if expressao:
            try:
                # Limpa a expressão, permitindo apenas dígitos, operadores (+-*/), ponto, parênteses e espaços.
                # Isso ajuda a prevenir injeção de código ou caracteres indesejados.
                expressao_limpa = ''.join(
                    c for c in expressao if c in '0123456789+-*/.() '
                )

                # Avalia a expressão limpa usando o interpretador 'asteval' e converte o resultado para string.
                resultado = str(aeval(expressao_limpa))

                # 'asteval' pode retornar 'None' para expressões inválidas ou incompletas, tratamos como 'Erro'.
                if resultado == 'None':
                    resultado = 'Erro'
                else:
                    # Se o resultado for válido, salva a operação no histórico do banco de dados.
                    Operacao.objects.create(
                        usuario=request.user, parametros=expressao, resultado=resultado
                    )
            except Exception:
                # Captura qualquer exceção durante a avaliação da expressão e define o resultado como 'Erro'.
                resultado = 'Erro'

            # Armazena o último resultado na sessão do usuário.
            # Isso é útil para exibir o resultado na próxima requisição GET (após o redirecionamento).
            request.session['last_result'] = resultado

            # Redireciona para a própria página da calculadora (GET) para evitar reenvio do formulário.
            return redirect('calculator')

    # Após um redirecionamento POST, ou na primeira vez que a página é carregada (GET),
    # tenta recuperar o último resultado da sessão e o remove dela.
    resultado = request.session.pop('last_result', '')

    # Renderiza o template da calculadora, passando o histórico e o resultado para exibição.
    return render(
        request,
        'calculator/calculator.html',
        {
            'historico': historico,  # Lista das últimas operações do usuário.
            'resultado': resultado,  # O resultado do último cálculo (se houver).
        },
    )


@login_required(
    login_url='login'
)  # Garante que apenas usuários logados podem acessar esta view.
def limpar_historico(request):
    """
    Função de visualização para limpar o histórico de operações de um usuário.
    Só processa requisições POST para evitar limpeza acidental.
    """
    # Verifica se a requisição é um POST (envio do formulário de limpeza).
    if request.method == 'POST':
        # Deleta todas as operações associadas ao usuário logado.
        Operacao.objects.filter(usuario=request.user).delete()

    # Redireciona o usuário de volta para a página da calculadora após a limpeza.
    return redirect('calculator')
