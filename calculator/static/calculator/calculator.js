// Aguarda o carregamento completo do DOM antes de executar o script.
document.addEventListener('DOMContentLoaded', function () {
  // Obtém referências para os elementos HTML principais da calculadora.
  const display = document.getElementById('display'); // Onde os números e resultados são exibidos.
  const buttons = document.querySelectorAll('.calc-buttons .btn'); // Todos os botões da calculadora.
  const form = document.getElementById('calc-form'); // O formulário que será submetido.
  const input = document.getElementById('expressao-input'); // O campo de input escondido no formulário.

  // Variável para armazenar a expressão matemática atual digitada.
  let current = '';
  // Flag que indica se o resultado de uma operação anterior acabou de ser exibido no display.
  // Isso ajuda a zerar o display ao iniciar uma nova operação.
  let resultJustShown = Boolean(
    display.textContent && display.textContent !== '0'
  );

  /**
   * Atualiza o conteúdo do display da calculadora.
   * @param {string} val - O valor a ser exibido. Se for vazio, exibe '0'.
   */
  function updateDisplay(val) {
    display.textContent = val || '0';
  }

  /**
   * Zera a expressão atual ('current') e o display,
   * caso um resultado tenha acabado de ser mostrado.
   * Isso prepara a calculadora para uma nova entrada.
   */
  function clearResultOnInput() {
    if (resultJustShown) {
      current = '';
      updateDisplay(current);
      resultJustShown = false; // Reseta a flag após limpar o display.
    }
  }

  // Adiciona um 'event listener' de clique a cada botão da calculadora.
  buttons.forEach((btn) => {
    btn.addEventListener('click', function () {
      // Obtém o valor e a ação associados ao botão clicado.
      const val = btn.getAttribute('data-value');
      const action = btn.getAttribute('data-action');

      // Lógica para diferentes ações dos botões.
      if (action === 'clear') {
        // Botão 'C' (Limpar): Zera a expressão e o display.
        current = '';
        updateDisplay(current);
      } else if (action === 'equals') {
        // Botão '=' (Igual): Se houver uma expressão, a submete via formulário.
        if (current) {
          input.value = current; // Define o valor do input escondido.
          form.submit(); // Envia o formulário.
        }
      } else if (action === 'negate') {
        // Botão '+/-' (Negar): Inverte o sinal do número atual.
        clearResultOnInput(); // Limpa o resultado anterior, se houver.
        if (current) {
          if (current.startsWith('-')) {
            current = current.slice(1); // Remove o '-' se já for negativo.
          } else {
            current = '-' + current; // Adiciona o '-' se for positivo.
          }
          updateDisplay(current);
        }
      } else if (action === 'percent') {
        // Botão '%' (Porcentagem): Converte o número atual em sua representação percentual.
        clearResultOnInput(); // Limpa o resultado anterior, se houver.
        if (current) {
          try {
            // Tenta converter para float e dividir por 100.
            current = (parseFloat(current) / 100).toString();
            updateDisplay(current);
          } catch (e) {
            // Ignora erros na conversão, caso o valor não seja numérico.
          }
        }
      } else {
        // Demais botões (números e operadores).
        clearResultOnInput(); // Limpa o resultado anterior, se houver.
        // Mapeia operadores de exibição para operadores de cálculo para o backend.
        let toAdd = val;
        if (val === '×') toAdd = '*'; // Multiplicação
        if (val === '÷') toAdd = '/'; // Divisão
        if (val === '−') toAdd = '-'; // Subtração (unicode para compatibilidade visual)
        if (val === '+') toAdd = '+'; // Adição
        current += toAdd; // Adiciona o caractere à expressão atual.
        updateDisplay(current); // Atualiza o display.
      }
    });
  });

  // Adiciona um 'event listener' para eventos de teclado (keydown).
  document.addEventListener('keydown', function (e) {
    // Permite usar a tecla Backspace para apagar caracteres.
    if (e.key === 'Backspace') {
      clearResultOnInput(); // Limpa o resultado anterior, se houver.
      current = current.slice(0, -1); // Remove o último caractere da expressão.
      updateDisplay(current); // Atualiza o display.
      e.preventDefault(); // Previne o comportamento padrão do navegador (voltar página).
    }
    // Permite usar a tecla Enter para submeter a expressão.
    if (e.key === 'Enter') {
      if (current) {
        input.value = current; // Define o valor do input escondido.
        form.submit(); // Envia o formulário.
      }
      e.preventDefault(); // Previne o comportamento padrão do navegador (submeter formulário ou nova linha).
    }
  });

  // Adiciona uma classe CSS ao display se um resultado acabou de ser mostrado.
  // Isso pode ser usado para estilos visuais específicos para o estado "resultado".
  if (resultJustShown) {
    display.classList.add('result-just-shown');
  }
});
