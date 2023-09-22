#Coleções (item B)

animais = ('CACHORRO','GATO')

usuario = input('Digite o nome de um animal:').upper()

if usuario in animais:
    print('Seu animal está na lista.')
else:
    print('Seu animal não está na lista.')
