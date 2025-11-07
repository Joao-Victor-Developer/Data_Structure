from collections import deque
import time

fila_pedidos = deque()

def mostrar_pedidos():
    if fila_pedidos:
        print("\n Pedidos na fila:")
        for i, pedido in enumerate(fila_pedidos, 1):
            print(f"{i}. {pedido}")
    else:
        print("\nNenhum pedido na fila.")

while True:
    print("\n--- LANCHONETE ---")
    print("1 - Fazer pedido")
    print("2 - Preparar próximo pedido")
    print("3 - Ver fila de pedidos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pedido = input("Digite o nome do pedido: ")
        fila_pedidos.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    elif opcao == "2":
        if fila_pedidos:
            preparando = fila_pedidos.popleft()
            print(f"Preparando '{preparando}'...")
            time.sleep(3)  
            print(f"'{preparando}' está pronto!")
        else:
            print("Nenhum pedido para preparar.")

    elif opcao == "3":
        mostrar_pedidos()

    elif opcao == "4":
        print("Fechando o sistema da lanchonete...")
        break

    else:
        print("Opção inválida! Tente de novo.")
