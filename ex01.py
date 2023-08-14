## Crie um programa que tenha uma dupla totalmente preenchida Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.##

cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
        'seis','sete','oito', 'nove', 'dez',
        'onze','doze','treze','catorze','quinze',
        'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input("diga um numero [o e 20]:"))
    if 0 <= num <= 20:
        break
    print("Tente novamente ", end=" ")
print(f'Você digitou {cont[num]}')
while True:
    deseja = str(input("Deseja continuar ? [S/N}:")).strip().upper()[0]
    if deseja == "S":
        num = int(input("diga um numero [o e 20]:"))

        print(f'Você digitou {cont[num]}')
    elif deseja == "N":
        break

