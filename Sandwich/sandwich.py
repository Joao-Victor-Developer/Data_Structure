pilha = []

while True:
    print("\n--- Montagem do Sanduíche ---")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche completo")
    print("5 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ingrediente = input("Digite o nome do ingrediente: ")
        pilha.append(ingrediente)
        print(f"Ingrediente '{ingrediente}' adicionado ao sanduíche.")

    elif opcao == "2":
        if len(pilha) > 0:
            removido = pilha.pop()
            print(f"Ingrediente '{removido}' removido do topo.")
        else:
            print("O sanduíche está vazio! Nada para remover.")

    elif opcao == "3":
        if len(pilha) > 0:
            print(f"O último ingrediente adicionado foi: '{pilha[-1]}'")
        else:
            print("O sanduíche ainda está vazio!")

    elif opcao == "4":
        if len(pilha) > 0:
            print("\n--- Seu sanduíche ---")
            for ingrediente in pilha:
                print(f"- {ingrediente}")
            print("---------------------")
        else:
            print("Nenhum ingrediente no sanduíche.")

    elif opcao == "5":
        print("Pedido finalizado! Bom apetite!")
        break

    else:
        print("Opção inválida. Tente novamente.")