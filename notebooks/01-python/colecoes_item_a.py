#Coleções (item A)
from random import randint
lista = []
for i in range(0,5):
    lista.append(randint(1,100))
    

for i in range(0,5):
    print(f'{i+1}º item =  {lista[i]}')


