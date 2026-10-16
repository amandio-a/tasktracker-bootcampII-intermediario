
def main():
    tarefas = []

    while True:
        print("\n===== TASKTRACKER =====")
        print("1 - Cadastrar nova tarefa")
        print("2 - Visualizar tarefas cadastradas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("Cadastro de tarefas em desenvolvimento.")

        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa cadastrada no momento.")

        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()

