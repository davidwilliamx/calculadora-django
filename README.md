# Calculadora Avançada com Histórico de Operações

Este projeto consiste num portal web que integra uma calculadora funcional, capaz de realizar operações básicas (soma, subtração, multiplicação e divisão). A aplicação foi desenvolvida com um sistema robusto de autenticação (login e senha) e uma funcionalidade essencial de registo de histórico, que armazena todas as operações realizadas por cada utilizador num banco de dados local. O histórico é exibido de forma conveniente ao lado da calculadora, permitindo aos utilizadores reverem os seus cálculos anteriores.

Este projeto foi desenvolvido como parte de um desafio técnico proposto pela Kogui, com o objetivo de demonstrar habilidades em desenvolvimento web com Django, gestão de bases de dados e lógica de programação.

## O Desafio

O principal objetivo era criar um portal interativo com uma calculadora, garantindo que as operações fossem persistidas num banco de dados local por utilizador. Os requisitos incluíam:

* Implementação de um sistema de login e senha.
* Capacidade de realizar operações de soma, subtração, multiplicação e divisão.
* Gravação dos parâmetros da operação (ex: "1+2") e do resultado (ex: "3") no banco de dados.
* Exibição do histórico de operações mais recentes para o utilizador logado.

## Como a aplicação atende ao desafio proposto

Este projeto foi desenvolvido para responder ao desafio técnico da Kogui, que propõe a criação de um portal com uma calculadora capaz de realizar operações básicas, com autenticação e histórico de operações por usuário. A seguir, detalhamos como cada requisito do desafio é atendido pela aplicação:

### Problemas/Desafios Propostos

- **1. Página de Login e Senha:**
  O desafio exige que o portal tenha autenticação via login e senha, garantindo acesso individualizado para cada usuário.

- **2. Operações Matemáticas:**
  A calculadora deve permitir operações de soma, subtração, multiplicação e divisão.

- **3. Persistência dos Cálculos:**
  Cada operação realizada deve ser registrada em um banco de dados local, associada ao usuário que realizou a operação.

- **4. Visualização do Histórico:**
  O usuário deve poder visualizar as últimas operações realizadas.

- **5. Estrutura de Dados conforme Diagrama:**
  O banco deve conter as tabelas `Usuario` e `Operacao`, com relacionamento 1:N, conforme o diagrama relacional apresentado.

- **6. Utilização do Django e SQLite:**
  O framework a ser utilizado é o Django, com banco de dados local SQLite.

---

### Como a aplicação resolve cada requisito

- **Autenticação de Usuários:**
  Utiliza o sistema nativo de autenticação do Django (`django.contrib.auth`).
  - O registro de novos usuários é feito com formulário próprio, mas baseado no modelo padrão do Django.
  - O login usa o `AuthenticationForm` do Django e funções nativas para autenticação e gerenciamento de sessão.
  - As senhas são armazenadas de forma segura com hash.

- **Operações Matemáticas:**
  A interface da calculadora permite realizar soma, subtração, multiplicação e divisão.
  - As expressões são avaliadas com segurança utilizando a biblioteca `asteval`, evitando riscos de execução de código malicioso.

- **Persistência de Dados e Histórico:**
  Cada operação realizada é salva na tabela `Operacao`, associada ao usuário autenticado, usando o ORM do Django e o banco SQLite.
  - O histórico das últimas operações é exibido na interface da calculadora, recuperando os dados diretamente do banco.

- **Estrutura de Dados conforme o Diagrama:**
  O modelo segue a estrutura proposta:
  - Usuários são representados pelo modelo padrão `User` do Django.
  - Operações são armazenadas em um modelo específico (`Operacao`), com chave estrangeira para o usuário.
  - O relacionamento 1:N entre usuário e operação é garantido pelo campo de chave estrangeira.

- **Uso do Django e SQLite:**
  O projeto está estruturado como uma aplicação Django padrão, utilizando SQLite como banco de dados local, conforme solicitado.

- **Boas Práticas e Clareza de Código:**
  O código é modular, organizado e segue a orientação a objetos e as melhores práticas recomendadas pelo Django.

---

Desta forma, a aplicação cobre todos os pontos do desafio, entregando um portal funcional, seguro e aderente aos requisitos propostos.

## Funcionalidades

* **Calculadora Interativa:** Interface amigável para realizar as quatro operações aritméticas fundamentais.
* **Sistema de Autenticação:** Registo e login de utilizadores para acesso personalizado à aplicação.
* **Histórico de Operações por Utilizador:** Cada operação realizada é associada ao utilizador, permitindo um histórico individualizado.
* **Persistência de Dados:** Armazenamento seguro das operações e dados do utilizador num banco de dados local.
* **Visualização do Histórico:** Exibição dinâmica dos últimos cálculos realizados na interface da calculadora.

## Tecnologias Utilizadas

* **Framework Web:** [Django](https://www.djangoproject.com/)
* **Linguagem de Programação:** [Python](https://www.python.org/)
* **Banco de Dados:** [SQLite](https://www.sqlite.org/index.html) (configurado como banco de dados local padrão do Django)
* **Front-end:** HTML, CSS, JavaScript (para a lógica da calculadora e interatividade)
* **Avaliação de Expressões:** `asteval` (para avaliação segura de expressões matemáticas)

## Considerações de Segurança: Por Que `asteval`?

No desenvolvimento desta calculadora, foi tomada a decisão crucial de utilizar a biblioteca `asteval` para avaliar as expressões matemáticas inseridas pelos utilizadores, em vez da função `eval()` nativa do Python. Esta escolha foi motivada por importantes razões de segurança.

### Os Perigos de `eval()`

A função `eval()` do Python é extremamente poderosa, permitindo a execução de qualquer código Python válido a partir de uma string. Contudo, essa flexibilidade representa uma **vulnerabilidade de segurança grave** em aplicações web que processam entrada de utilizadores. Se um utilizador mal-intencionado inserisse código arbitrário (como comandos para excluir arquivos, aceder a dados sensíveis ou iniciar ataques de negação de serviço), `eval()` o executaria diretamente no servidor, comprometendo a segurança da aplicação e do sistema.

### Como `asteval` Resolve o Problema

`asteval` (Abstract Syntax Tree Evaluator) é uma biblioteca projetada especificamente para avaliar expressões matemáticas e lógicas de forma **segura e controlada**. Diferente de `eval()`, `asteval` opera num ambiente "sandboxed" (isolado), o que significa que:

1.  **Análise da Árvore de Sintaxe Abstrata (AST):** Primeiro, a string de entrada é analisada e convertida numa Árvore de Sintaxe Abstrata. Isso permite que `asteval` compreenda a estrutura da expressão sem a executar diretamente.
2.  **Ambiente Controlado:** A avaliação ocorre num ambiente restrito, sem acesso a funcionalidades perigosas do sistema, como importação de módulos (`os`, `sys`), acesso ao sistema de arquivos ou execução de comandos externos.
3.  **Controle Explícito:** É possível definir explicitamente quais funções e variáveis são permitidas dentro do ambiente de avaliação, garantindo controlo total sobre as operações que podem ser realizadas.

Dessa forma, `asteval` permite que os utilizadores insiram expressões complexas como "5+2\*3/4" sem que a aplicação corra o risco de execução de código malicioso, tornando a calculadora robusta e segura.

### Uso de `asteval` no Projeto

No projeto, `asteval` é utilizado na `views.py` do aplicativo `core` (ou onde a lógica da calculadora estiver implementada). O fluxo é o seguinte:

1.  A expressão matemática inserida pelo utilizador é capturada.
2.  Uma nova instância do `asteval.Interpreter` é criada para garantir um ambiente de avaliação limpo e isolado para cada cálculo.
3.  A expressão é passada para o interpretador (`aeval(expressao)`).
4.  É realizada uma verificação de erros (`aeval.error`) para identificar e reportar ao utilizador quaisquer problemas na sintaxe ou na lógica da expressão (ex: divisão por zero).
5.  Se a avaliação for bem-sucedida e sem erros, o resultado é obtido e a operação (expressão e resultado) é persistida no modelo `Operacao` associado ao utilizador logado.

Este método garante que a funcionalidade da calculadora seja mantida, ao mesmo tempo que protege a aplicação contra potenciais ataques de injeção de código.

## Estrutura do Banco de Dados

O modelo de dados segue o diagrama de objetos relacionais fornecido, com duas entidades principais: `Usuario` e `Operacao`.

### Tabela `Usuario`

Responsável por armazenar as informações dos utilizadores do sistema.

| Campo        | Tipo              | Descrição                                         |
| :----------- | :---------------- | :------------------------------------------------ |
| `IDUsuario`  | `INT PRIMARY KEY` | Identificador único e primário do utilizador.     |
| `Nome`       | `VARCHAR NOT NULL`| Nome completo do utilizador.                      |
| `Email`      | `VARCHAR NOT NULL`| Endereço de e-mail do utilizador (único).         |
| `Senha`      | `VARCHAR NOT NULL`| Senha do utilizador (deve ser armazenada com hash).|
| `DtInclusao` | `DATETIME NOT NULL`| Data e hora de criação do registo do utilizador.  |

### Tabela `Operacao`

Armazena os detalhes de cada cálculo realizado.

| Campo        | Tipo              | Descrição                                         |
| :----------- | :---------------- | :------------------------------------------------ |
| `IDOperacao` | `INT PRIMARY KEY` | Identificador único e primário da operação.       |
| `IDUsuario`  | `INT FOREIGN KEY` | Chave estrangeira que referencia `IDUsuario` da tabela `Usuario`, indicando qual utilizador realizou a operação. |
| `Parametros` | `VARCHAR NOT NULL`| A expressão da operação (ex: "1+2", "5*3").       |
| `Resultado`  | `VARCHAR NOT NULL`| O resultado da operação (ex: "3", "15").          |
| `DtInclusao` | `DATETIME NOT NULL`| Data e hora em que a operação foi registada.      |

A relação entre `Usuario` e `Operacao` é de **um para muitos (1:N)**, o que significa que um único utilizador pode ter múltiplas operações registadas, mas cada operação pertence a apenas um utilizador.

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/installation/) (geralmente incluído com Python) instalados no seu sistema.

### Passos de Instalação e Execução (Método Tradicional)

1.  **Clone o Repositório:**
    Comece por clonar o projeto do GitHub para a sua máquina local:
    ```bash
    git clone https://github.com/davidwilliamx/calculadora-django.git
    cd calculadora-django
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    É uma boa prática isolar as dependências do projeto num ambiente virtual.
    ```bash
    python -m venv venv
    ```
    Ative o ambiente virtual:
    * **No Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **No macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as Dependências:**
    Instale todas as bibliotecas Python necessárias listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
    **Conteúdo Sugerido para `requirements.txt`:**
    ```
    Django>=3.2,<5.0
    asteval>=0.9.1 # Adicionado para avaliação segura de expressões
    # Adicione outras dependências se necessário (ex: djangorestframework, psycopg2, etc.)
    ```

4.  **Execute as Migrações do Banco de Dados:**
    Este comando cria as tabelas do banco de dados (`Usuario`, `Operacao`, e outras tabelas padrão do Django) com base nos modelos definidos.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário (Opcional):**
    Se desejar aceder ao painel de administração do Django para gerir utilizadores ou operações diretamente, crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para definir o nome de utilizador, e-mail e senha.

6.  **Inicie o Servidor de Desenvolvimento:**
    Finalmente, inicie o servidor local do Django:
    ```bash
    python manage.py runserver
    ```
    A aplicação estará acessível no seu navegador em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

A estrutura de diretórios do projeto deve ser semelhante a esta:

```
.
├── calculadora_project/       # Diretório principal do projeto Django (configurações globais)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configurações do projeto (banco de dados, apps, etc.)
│   ├── urls.py                # Rotas URL globais do projeto
│   └── wsgi.py
├── core/                      # Aplicativo Django principal para a lógica da calculadora e autenticação
│   ├── migrations/            # Migrações do banco de dados para os modelos do app 'core'
│   ├── __init__.py
│   ├── admin.py               # Registo de modelos para o painel de administração
│   ├── apps.py
│   ├── models.py              # Definição dos modelos `Usuario` e `Operacao`
│   ├── tests.py
│   ├── views.py               # Lógica de negócio para as páginas (login, registo, calculadora)
│   ├── urls.py                # Rotas URL específicas do app 'core'
│   └── templates/             # Templates HTML para as views
│       ├── registration/      # Templates para autenticação (login, registo, etc.)
│       │   └── login.html
│       │   └── register.html
│       └── calculator.html    # Template da página da calculadora
├── static/                    # Diretório para arquivos estáticos (CSS, JavaScript, imagens)
│   ├── css/
│   ├── js/
│   └── img/
├── media/                     # Diretório para arquivos de mídia enviados por utilizadores (se aplicável)
├── manage.py                  # Script de linha de comando do Django
├── db.sqlite3                 # Arquivo do banco de dados SQLite (gerado após `migrate`)
├── requirements.txt           # Lista de dependências Python do projeto
├── Dockerfile                 # Arquivo para construir a imagem Docker da aplicação
├── docker-compose.yml         # Arquivo para orquestrar a execução do container Docker
└── README.md                  # Este arquivo
```

## Critérios de Avaliação (Conforme o Desafio Kogui)

Este projeto foi desenvolvido com foco nos seguintes critérios de avaliação:

* **Clareza e Organização de Código:** O código é estruturado de forma lógica, com nomes de variáveis e funções descritivos, e comentários quando necessário, visando facilitar a leitura e manutenção.
* **Lógica de Programação:** A implementação das funcionalidades segue uma lógica clara e eficiente, garantindo o correto funcionamento da calculadora e do sistema de histórico.
* **Aplicação da Programação Orientada a Objetos (POO):** Os modelos, views e outras componentes do Django são projetados seguindo os princípios de POO, promovendo a modularidade, reutilização e extensibilidade do código.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* no repositório.

---
Desenvolvido com ❤ por [David Magalhães]
