
fila = []
while True:
    print("1 informar nome")
    print("2 Atender pessoa")
    print("3 mostrar fila")
    print("4 Sair")
    escolha = input("Faça sua escolha")
    if escolha == "1":
        nome = input("digite o nome")
        fila.append(nome)
    elif escolha == "2":
        print("Atender")
        if len(fila) > 0:
            print("Atendido", fila.pop(0))
        else:
            print("Fila seca")
    elif escolha == "3":
        print(fila)
    elif escolha == "4":
        print("Sair")
        break
    
    else:
        print("Opção inválida")
        
        


