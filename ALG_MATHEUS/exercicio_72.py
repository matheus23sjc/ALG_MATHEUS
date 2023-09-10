deposito = float(input('\n Entre com um deposito: '))
taxa = float(input('\n Entre com a taxa de juros: '))
valor = deposito*taxa/100
total = deposito+valor

print(f'\n Rendimentos: {valor} \n Total: {total}')
print('\n')
