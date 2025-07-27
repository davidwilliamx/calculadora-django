from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    """
    Formulário para registro de novos usuários.
    Herda de forms.ModelForm para se integrar ao modelo User do Django
    e adiciona validação personalizada para a confirmação de senha.
    """

    # Campo para a senha do usuário, exibido como input de senha.
    password = forms.CharField(widget=forms.PasswordInput)
    # Campo extra para confirmar a senha, também exibido como input de senha.
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirme a senha"
    )

    class Meta:
        # Define que este formulário está associado ao modelo 'User'.
        model = User
        # Especifica quais campos do modelo 'User' serão usados no formulário.
        fields = ['username', 'email', 'password']

    def clean(self):
        """
        Método de validação personalizado para garantir que as senhas coincidam.
        É chamado após a validação individual de cada campo.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Verifica se as senhas digitadas são diferentes.
        if password != password_confirm:
            # Se forem diferentes, levanta um erro de validação.
            raise forms.ValidationError("As senhas não coincidem.")

        # Retorna os dados limpos se a validação for bem-sucedida.
        return cleaned_data
