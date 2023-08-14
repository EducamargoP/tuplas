## : Crie um programa que tenha uma tupla com várias palavras, para cada palavra, quais são as suas vogais.

texto = ('BASQUETE', 'FUTEBOL', 'VOLEI', 'NATACAO', 'JOGAR', 'CORRER', 'ANDAR', 'NADAR')

for C in texto:
   print (f"\n a palavra {C} tem tantas vogais ", end= " ")
   for letra in C:
       if letra in 'AEIOU':
           print(letra, end=' ')
