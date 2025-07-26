from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirme a senha"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data


"""
Este código define um formulário de registro de usuário em Django, projetado para interagir com o modelo de usuário padrão do Django (`django.contrib.auth.models.User`).

*   **Importações:** Ele importa o módulo `forms` do Django para criar formulários e o modelo `User` para vincular o formulário a ele.
*   **Classe `RegisterForm`:** Esta classe herda de `forms.ModelForm`, o que significa que ela é diretamente ligada a um modelo (neste caso, o modelo `User`).
*   **Campos Personalizados:**
    *   `password`: Um campo de texto (`CharField`) que usa o widget `PasswordInput` para ocultar os caracteres digitados, adequado para senhas.
    *   `password_confirm`: Outro campo de texto (`CharField`) com `PasswordInput`, usado para confirmar a senha. Possui um rótulo personalizado "Confirme a senha". Este campo não é parte do modelo `User` em si, mas é adicionado ao formulário para fins de validação.
*   **Classe `Meta`:**
    *   `model = User`: Indica que este `ModelForm` está associado ao modelo `User` do Django.
    *   `fields = ['username', 'email', 'password']`: Especifica quais campos do modelo `User` devem ser incluídos no formulário. É importante notar que `password_confirm` não está nesta lista, pois é um campo auxiliar apenas para validação, não um campo que será salvo diretamente no modelo `User`.
*   **Método `clean()`:**
    *   Este método é um gancho de validação em nível de formulário no Django. Ele é executado depois que os campos individuais são limpos e validados.
    *   `cleaned_data = super().clean()`: Chama o método `clean` da classe pai para garantir que a validação padrão do formulário seja executada primeiro e para obter os dados já limpos.
    *   Ele recupera os valores dos campos `password` e `password_confirm`.
    *   `if password != password_confirm:`: Realiza uma verificação para garantir que as duas senhas inseridas coincidam.
    *   `raise forms.ValidationError("As senhas não coincidem.")`: Se as senhas não coincidirem, uma exceção `ValidationError` é levantada, o que impede que o formulário seja considerado válido e exibe a mensagem de erro fornecida ao usuário.
    *   `return cleaned_data`: Se as senhas coincidirem, os dados limpos do formulário são retornados, permitindo que o processamento do formulário continue.

Em resumo, este código cria um formulário de registro de usuário que solicita um nome de usuário, e-mail e permite que o usuário insira e confirme uma senha, garantindo que as duas entradas de senha correspondam antes de permitir o envio.

"""
