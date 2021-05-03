# ToDo List EVOE

Uma ToDo List simples construída com Django e Django Rest Framework.

A lista pode ser acessada tanto por uma interface web quanto por uma API. As tarefas e credenciais são compartilhadas entre as duas formas de acesso. Usuários podem visualizar uma lista com suas tarefas cadastradas ou os detalhes de cada tarefa individualmente. É possível cadastrar novas tarefas com título e descrição e definir se a tarefa é importante ou não. Também há páginas e endpoints para que usuários possam editar ou deletar tarefas existentes. Um usuário só pode visualizar ou manipular suas próprias tarefas.

## Web

A página web pode ser acessada em: http://todo.eba-f4dqfau6.us-east-2.elasticbeanstalk.com

## API

A documentação da API pode ser acessada em http://todo.eba-f4dqfau6.us-east-2.elasticbeanstalk.com/readthedocs

## Sobre o projeto

### Estrutura

Os serviços estão hospedados no Elastic Beanstalk da AWS, utilizando como banco de dados uma instância PostgreSQL hospedada no RDS da AWS.

### Versão local

Para rodar uma versão local do projeto (é recomendável utilizar uma venv):

* git clone
* pip install -r requirements.txt
    * em sistemas linux pode ser necessário instalar a biblioteca linux libpq como dependência da python biblioteca psycopg2. 
    * em distribuições ubuntu: sudo apt-get install libpq-dev
    * isso só será necessário para utilizar o postgres como banco de dados, caso pretenda utilizar apenas a instalação local com sqlite, é possível remover a dependência psycopg2 do arquivo requirements.txt e não instalar a libpq.
* configurar uma variável de ambiente EVOE_KEY como chave de segurança do Django.
* na pasta evoe (onde está o arquivo settings.py) criar um arquivo com nome local_settings.py e conteúdo:

    DEBUG = True
    
    ALLOWED_HOSTS = []

* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* o serviço web deve ser acessado em http://127.0.0.1:8000 e a api em http://127.0.0.1:8000/api/

#### Troubleshooting versão local

* Caso o Django acuse que determinada tabela não existe no banco de dados, executar:
    * python manage.py migrate --run-syncdb


### Estrutura do projeto Django
    evoe-todo
    |_ api
    |_ evoe
    |_ todo
        |_ static
            |_ todo
        |_ templates
            |_ docs
            |_ registration
            |_ todo
    |_ manage.py

* api: app Django para a api
* evoe: diretório do projeto Django
* todo: app Django para o serviço web
    * static/todo: arquivos .css e .js
    * templates
        * docs: templates da documentação da api
        * registration: templates das páginas de registro, login e logout
        * todo: templates do serviço web 


### Testes

Para executar os testes, navegar até o diretório evoe-todos (que contém o arquivo manage.py) e executar

    python manage.py test todo
    python manage.py test api


### Escolhas

Algumas escolhas foram tomadas com o intuito de manter a simplicidade do projeto, como:

* Um perfil extremamente simplificado, apenas com nome de usuário e senha.
* Ausência de um processo de reset de senha.
* Ausência de validação da forma da senha (número de caracteres, maiúsculas e minúsculas, etc).
* Uso do sistema e das páginas de autenticação padronizados do Django.

### Pontos de melhoria

* Aprimoramento das views de ambos os serviços para fortalecer a lógica de cada operação, para evitar falhas e comportamentos inesperados.
* Mais atenção ao modelo e perfil dos usuários.
* Front end e identidade visual.
* Sistema de autenticação.

### Comentários pessoais

Esse foi meu primeiro contato com o Django Rest Framework, apesar de já ter alguma experiência com Django construindo páginas pessoais. Por isso fazer esse projeto foi muito legal! Foi uma ótima oportunidade para aprender uma ferramenta nova que certamente vai me ser muito útil. Já estou vendo a oportunidade de aplicar o que aprendi aqui em outros projetos que mantenho para melhorá-los. Muito obrigado! :)
