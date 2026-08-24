# Exercício 07 - Contadores e acumuladores em Python
quantidade = int(input("Quantidade de pedidos: "))

if quantidade <= 0:
    print("Quantidade inválida.")
else:
    total_vendas = 0.0
    pedidos_pequenos = 0
    pedidos_medios = 0
    pedidos_grandes = 0

    for numero_pedido in range(1, quantidade + 1):
        valor = float(input(f"Valor do pedido {numero_pedido}: R$ ").replace(",", ".'))
        total_vendas += valor

        if valor < 20:
            pedidos_pequenos += 1
        elif valor < 50: 
            pedidos_medios += 1
        else:
            pedidos_grandes += 1

    ticket_medio = total_vendas / quantidade
    print(f"\nTotal vendido: R$ {total_vendas:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Pedidos pequenos: {pedidos_pequenos}")
    print(f"Pedidos médios: {pedidos_medios}")
    print(f"Pedidos grandes: {pedidos_grandes}")