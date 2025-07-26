document.addEventListener('DOMContentLoaded', function () {
  const display = document.getElementById('display');
  const buttons = document.querySelectorAll('.calc-buttons .btn');
  const form = document.getElementById('calc-form');
  const input = document.getElementById('expressao-input');

  let current = '';
  let resultJustShown = Boolean(
    display.textContent && display.textContent !== '0'
  );

  function updateDisplay(val) {
    display.textContent = val || '0';
  }

  // Zera resultado ao clicar em qualquer botão (exceto igual)
  function clearResultOnInput() {
    if (resultJustShown) {
      current = '';
      updateDisplay(current);
      resultJustShown = false;
    }
  }

  buttons.forEach((btn) => {
    btn.addEventListener('click', function () {
      const val = btn.getAttribute('data-value');
      const action = btn.getAttribute('data-action');
      if (action === 'clear') {
        current = '';
        updateDisplay(current);
      } else if (action === 'equals') {
        if (current) {
          input.value = current;
          form.submit();
        }
      } else if (action === 'negate') {
        clearResultOnInput();
        if (current) {
          if (current.startsWith('-')) current = current.slice(1);
          else current = '-' + current;
          updateDisplay(current);
        }
      } else if (action === 'percent') {
        clearResultOnInput();
        if (current) {
          try {
            current = (parseFloat(current) / 100).toString();
            updateDisplay(current);
          } catch (e) {}
        }
      } else {
        clearResultOnInput();
        // Operadores × e ÷ substituídos por * e / para backend
        let toAdd = val;
        if (val === '×') toAdd = '*';
        if (val === '÷') toAdd = '/';
        if (val === '−') toAdd = '-';
        if (val === '+') toAdd = '+';
        current += toAdd;
        updateDisplay(current);
      }
    });
  });

  // Permite backspace no teclado físico
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Backspace') {
      clearResultOnInput();
      current = current.slice(0, -1);
      updateDisplay(current);
      e.preventDefault();
    }
    if (e.key === 'Enter') {
      if (current) {
        input.value = current;
        form.submit();
      }
      e.preventDefault();
    }
  });

  // Zera resultado ao digitar no display pela primeira vez após mostrar resultado
  if (resultJustShown) {
    display.classList.add('result-just-shown');
  }
});

/**
 * Este código JavaScript gerencia a lógica de front-end de uma calculadora simples. Ele escuta eventos de cliques nos botões da calculadora e de teclas pressionadas no teclado para manipular a entrada e exibição de expressões.

Aqui está um detalhamento das suas funcionalidades:

    Inicialização (DOMContentLoaded): O código espera que todo o HTML seja carregado antes de começar a executar. Ele obtém referências aos elementos HTML principais: o display da calculadora, todos os botões, o formulário e um campo de input oculto para a expressão.
    Variáveis de Estado:
        current: Armazena a expressão matemática atual que está sendo construída pelo usuário.
        resultJustShown: Uma flag booleana que indica se um resultado acabou de ser exibido no display. Isso é usado para limpar a expressão atual quando o usuário começa a digitar um novo cálculo após ver um resultado.
    updateDisplay(val): Uma função utilitária que atualiza o texto do elemento display da calculadora. Se nenhum valor for fornecido, ele exibe '0'.
    clearResultOnInput(): Esta função verifica se um resultado acabou de ser exibido (resultJustShown). Se sim, ela zera a expressão current e atualiza o display, preparando a calculadora para uma nova entrada.
    Manipulação de Botões (buttons.forEach):
        Cada botão da calculadora recebe um ouvinte de evento de clique.
        Limpar (data-action="clear"): Zera a expressão current e o display.
        Igual (data-action="equals"): Se houver uma expressão em current, ele a atribui ao valor do campo de input oculto (input.value) e submete o formulário. Isso sugere que o cálculo real é feito por um backend.
        Negar (data-action="negate"): Adiciona ou remove um sinal de menos da expressão atual.
        Porcentagem (data-action="percent"): Divide o número atual por 100.
        Outros botões (números e operadores): Chamam clearResultOnInput() e adicionam o valor do botão à expressão current. Ele também substitui os caracteres de operador de exibição (×, ÷, −) pelos seus equivalentes de programação (*, /, -) antes de adicioná-los à current, provavelmente para compatibilidade com o backend.
    Manipulação de Teclado (document.addEventListener('keydown')):
        Backspace: Permite que o usuário apague o último caractere da expressão current usando a tecla Backspace. Também chama clearResultOnInput().
        Enter: Se houver uma expressão, ele submete o formulário, simulando o clique no botão "igual".
        Em ambos os casos, e.preventDefault() é usado para evitar o comportamento padrão do navegador (como navegar para trás ou submeter o formulário de forma não controlada).
    Estilo result-just-shown: Se a página carregar com um resultado já exibido no display, ele adiciona uma classe CSS result-just-shown ao display, que pode ser usada para aplicar estilos visuais específicos.


 */
