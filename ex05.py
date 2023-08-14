## Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços


listagem = ( 'lapis', 1.75,
             'borracha', 2.49,
             'caneta', 3.59,
             'apontador', 2.99,
             'caderno', 10.99,
             'mochila', 59.99)
print("="*30)
print("LISTA DE MATERIA ESCOLAR")
print("="*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem [pos]:.<30}", end="")
    elif pos % 2 == 1:
        print(f"R$: {listagem[pos]}")
print("="*30)