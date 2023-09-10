valor = int(input('\n digite o valor da prestação: '))
taxa = int(input('\n digite a taxa: '))
tempo = int(input('\n digite o tempo (numero de meses): '))
prest = valor+(valor*(taxa/100)*tempo)

print(f' \n O valor da prestação em atraso é: {prest}')
print('\n')
