# TaskTracker

Aplicação de gerenciamento de tarefas via interface de linha de comando (CLI), desenvolvida em Python 3 para o Bootcamp II de Engenharia de Software.

## Funcionalidades

- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação do título obrigatório, da prioridade (Alta, Média ou Baixa) e da data limite.
- Status inicial automático **Pendente**.
- Listagem de tarefas e resumo de status.

## Tecnologias

- Python 3 (biblioteca padrão)
- Git e GitHub para versionamento

## Como executar

1. Tenha Python 3 instalado.
2. Abra um terminal na pasta principal do projeto.
3. Execute:

   ```bash
   python src/main.py
   ```

   No Windows, também é possível usar `py src/main.py`.

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Observação

As tarefas são armazenadas apenas na memória durante a execução. Ao encerrar o programa, não ficam salvas. A persistência de dados não é exigida nesta fase.



## Execução com Docker

O TaskTracker pode ser executado em um contêiner Docker, permitindo utilizar a aplicação sem instalar o Python diretamente no computador.

### Pré-requisitos

- Docker Desktop instalado e em execução.
- Docker Compose disponível.
- Terminal PowerShell ou equivalente.

### 1. Construir a imagem Docker

Abra o terminal na pasta principal do projeto e execute:

```bash
docker build -t tasktracker .
```

Esse comando utiliza o Dockerfile para construir uma imagem com Python 3.11 e o código-fonte da aplicação.

### 2. Executar a aplicação com Docker

```bash
docker run -it --rm tasktracker
```

O parâmetro `-it` permite interagir com o menu pelo terminal, enquanto `--rm` remove o contêiner após o encerramento.

### 3. Executar com Docker Compose

```bash
docker compose run --rm tasktracker
```

O Docker Compose utiliza as configurações do arquivo `docker-compose.yml`, incluindo `stdin_open: true` e `tty: true`, necessárias para permitir a interação com o menu.

### Funcionalidades disponíveis

A aplicação permite cadastrar tarefas com título, descrição, prioridade e data limite, validar os dados informados e visualizar as tarefas cadastradas.

As tarefas são mantidas em memória durante a execução. Ao encerrar o programa, os registros não são persistidos.

### Encerramento

Para encerrar a aplicação, escolha a opção `3` no menu do TaskTracker.