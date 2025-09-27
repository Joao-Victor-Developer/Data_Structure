cor =  input("Digite a cor: ")


if cor != "azul" and cor != "vermelho" and cor != "amarelo":
    print("A cor escolhida não é primária")
elif cor == "vermelho" or cor == "Vermelho" or cor == "VERMELHO":
    print("A cor escolhida foi vermelho")
elif cor == "azul" or cor == "Azul" or cor == "AZUL":
    print("A cor escolhida foi azul")
elif cor == "amarelo" or cor == "Amarelo" or cor == "AMARELO":
    print("A cor escolhida foi amarelo")
else:
    print("A cor escolhida foi outra")