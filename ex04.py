## Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.

valor = (int(input("digite um numero : ")),
        int(input("digite outro numero :")),
        int(input("digite mais um numero :" )),
        int(input("digite ultimo numero :")))

print(f"Você digitou : {valor}")
print(f"Maior numero foi : {max(valor)}")
print(f"Menor numero foi : {min(valor)}")
print(f"O numero 9 apareceu {valor.count(3)} vezes")
if 3 in valor:
    print(f"O numero 3 apareceu na {valor.index(3)} posição")
else:
    print(f"O valor 3 não foi digitado!")
for c in valor:
    if c % 2 == 0:
        print(f"São tantos numero pares {c}")