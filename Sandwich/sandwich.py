pilha = []

while True:
  
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente ")
    print("3 - Ver ingrediente adicionado")
    print("4 - Mostrar sanduíche ")
    print("5 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ingrediente = input("Digite o nome do ingrediente: ")
        pilha.append(ingrediente)
        print(f"Ingrediente '{ingrediente}' adicionado.")

    elif opcao == "2":
        if len(pilha) > 0:
            removido = pilha.pop()
            print(f"Ingrediente '{removido}' removido")
        else:
            print("O sanduíche está vazio")

    elif opcao == "3":
        if len(pilha) > 0:
            print(f"O ingrediente adicionado foi: '{pilha[-1]}'")
        else:
            print("O sanduíche ainda está sem")

    elif opcao == "4":
        if len(pilha) > 0:
            print("--- Seu sanduíche ---")
            for ingrediente in pilha:
                print(f"- {ingrediente}")
           
        else:
            print("Nenhum ingrediente")

    elif opcao == "5":
        print("Pedido finalizado")
        break

    else:
        print("Opção inválida")