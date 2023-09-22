
def primo(numero):
    for i in range(2,int(numero)):
        if (numero%i) == 0:
            return print('Este número não é primo')
    return print('Este número é primo')