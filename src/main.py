from datetime import datetime, date


def solicitar_titulo():
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: O título é obrigatório!")


def solicitar_prioridade():
    prioridades = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in prioridades:
            return prioridades[entrada]
        print("Erro: informe somente Alta, Média ou Baixa.")


def solicitar_data_limite():
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data_limite = datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("Erro: digite uma data válida no formato DD/MM/AAAA.")
            continue
        if data_limite < date.today():
            print("Erro: a data limite não pode ser anterior à data atual.")
            continue
        return data_limite.strftime("%d/%m/%Y")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")
    titulo = solicitar_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = solicitar_prioridade()
    data_limite = solicitar_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")

    pendentes = sum(tarefa["status"] == "Pendente" for tarefa in tarefas)
    concluidas = sum(tarefa["status"] == "Concluída" for tarefa in tarefas)
    print(f"\nResumo: {pendentes} pendente(s) e {concluidas} concluída(s).")


def main():
    tarefas = []
    while True:
        print("\n===== TASKTRACKER =====")
        print("1 - Cadastrar nova tarefa")
        print("2 - Visualizar tarefas cadastradas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()