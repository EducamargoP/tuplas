from random import randint
## Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.


num = (randint (0,10),randint (0,10),randint (0,10),randint (0,10),randint (0,10),)

print(f"Os valores soteados foram : {num}")
print(f"O maior numero foi: {max(num)}")
print(f"O menor numero foi: {min(num)}")