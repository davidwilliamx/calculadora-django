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
