#Estruturas de seleção e repetição(item b)
#estruturas (item b)
from random import randint
numero_secreto = randint(1,100)
while True:
    numero_usuario = int(input('Digite um valor:'))
    
    if numero_usuario < numero_secreto:
        print('Seu número é menor que o número secreto\n')
    elif numero_usuario > numero_secreto:
        print('Seu número é maior que o número secreto\n')
    else:
        print('Parabéns . Este éo número secreto')
        break



