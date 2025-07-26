from django.db import models
from django.contrib.auth.models import User


class Operacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    parametros = models.CharField(max_length=100)  # Ex: "3+2"
    resultado = models.CharField(max_length=100)  # Ex: "5"
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parametros} = {self.resultado}"


"""
Este código define um modelo Django chamado `Operacao`. Este modelo é usado para representar uma operação que foi realizada por um usuário.

Detalhes dos campos:
*   **`usuario`**: Este é um campo de chave estrangeira (`ForeignKey`) que estabelece uma relação de muitos para um com o modelo `User` embutido do Django. Isso significa que cada `Operacao` está associada a um único usuário. O `on_delete=models.CASCADE` garante que se um usuário for excluído, todas as operações associadas a ele também serão excluídas.
*   **`parametros`**: Um campo de texto (`CharField`) com um comprimento máximo de 100 caracteres. Ele é destinado a armazenar os parâmetros de entrada da operação, como uma expressão matemática ("3+2").
*   **`resultado`**: Outro campo de texto (`CharField`) com um comprimento máximo de 100 caracteres. Este campo armazena o resultado da operação ("5").
*   **`dt_inclusao`**: Um campo de data e hora (`DateTimeField`). O argumento `auto_now_add=True` faz com que este campo seja preenchido automaticamente com a data e hora atuais no momento em que a operação é criada pela primeira vez, e não será atualizado em modificações posteriores.
*   **`__str__(self)`**: Este método especial define a representação em string de um objeto `Operacao`. Quando um objeto `Operacao` é impresso ou exibido no painel de administração do Django, ele mostrará uma string formatada como "parâmetros = resultado", por exemplo, "3+2 = 5".

Em resumo, este modelo serve para registrar operações realizadas por usuários, guardando os parâmetros de entrada, o resultado e o momento em que a operação foi registrada.
"""
