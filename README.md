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
