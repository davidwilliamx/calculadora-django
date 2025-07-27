from django.db import (
    models,
)  # Importa o módulo 'models' do Django, essencial para definir modelos de banco de dados.
from django.contrib.auth.models import (
    User,
)  # Importa o modelo 'User' padrão do Django, usado para associar operações a usuários.


class Operacao(models.Model):
    """
    Modelo que representa uma operação realizada por um usuário.
    Armazena os parâmetros da operação, seu resultado e a data de inclusão.
    """

    # Chave estrangeira para o modelo User. Quando um usuário é deletado,
    # todas as suas operações associadas também serão deletadas (CASCADE).
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Campo para armazenar os parâmetros da operação (ex: "3+2").
    # Define um tamanho máximo de 100 caracteres.
    parametros = models.CharField(max_length=100)

    # Campo para armazenar o resultado da operação (ex: "5").
    # Define um tamanho máximo de 100 caracteres.
    resultado = models.CharField(max_length=100)

    # Campo que armazena automaticamente a data e hora de criação da operação.
    # 'auto_now_add=True' define a data apenas na primeira vez que o objeto é salvo.
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retorna uma representação em string do objeto Operacao.
        Útil para visualização no painel administrativo do Django.
        """
        return f"{self.parametros} = {self.resultado}"
