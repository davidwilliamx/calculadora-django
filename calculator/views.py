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
