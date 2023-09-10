p = int(input('\n digite o valor da aplicação: '))
i = int(input('\n digite a taxa (0-1):'))
n = int(input('\n digite o numero de meses: '))
va = p* (((1+i)**n)-1)/i

print(f'\n O valor acumulado: {va}')
print('\n')