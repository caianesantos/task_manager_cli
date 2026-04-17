opcao = None

while opcao != 0:
    opcao = int(input("""
                    MENU:\n
                1- Criar nova tarefa; \n
                2- Listar tarefas; \n
                3- Atualizar tarefa; \n
                4- Deletar tarefa; \n
                0- Sair\n
                Selecione a opção desejada:
                """))
    if opcao == 1:
        print("Criando tarefa...")
    if opcao == 2:
        print("Listando tarefas...")
    if opcao == 3:
        print("Atualizando tarefa...")
    if opcao == 4:
        print("Deletando tarefa...")
    if opcao == 0:
        print("Encerrando...")
        break
    else:
        print("Não encontrada. Digite uma opção válida. ")
    

