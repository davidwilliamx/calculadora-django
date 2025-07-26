from django.apps import AppConfig


class CalculatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calculator'


"""
Este é um arquivo de configuração de aplicativo Django.

*   `from django.apps import AppConfig`: Esta linha importa a classe base `AppConfig` do módulo `django.apps`, que é necessária para criar uma configuração para um aplicativo Django.
*   `class CalculatorConfig(AppConfig):`: Define uma classe `CalculatorConfig` que herda de `AppConfig`. Esta classe é onde você configura metadados e comportamentos específicos para o aplicativo 'calculator'.
*   `default_auto_field = 'django.db.models.BigAutoField'`: Esta configuração especifica o tipo de campo de chave primária que será automaticamente adicionado aos modelos dentro deste aplicativo, caso não seja explicitamente definido. `BigAutoField` é um campo de inteiro de 64 bits, que oferece um intervalo maior para IDs do que o `AutoField` padrão, sendo útil para aplicativos que esperam um grande número de registros.
*   `name = 'calculator'`: Define o nome do aplicativo. Django usa este nome para se referir ao aplicativo em várias partes do framework, como ao carregar migrações ou ao identificar modelos.
"""
