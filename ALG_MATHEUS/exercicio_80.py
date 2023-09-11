quant = int(input('\n Digite a quantidade de fitas: '))
valAlug = float(input('\n Digite o valor do aluguel: '))
fatAnual = quant/3*valAlug*12

print(f'\n Faturamento anual: {fatAnual:.2f}')

multas = valAlug*0.1*(quant/3)/10

print(f'\n Multas mensais: {multas:.2f}')

quantFinal = (quant - quant * 0.02 + quant/10) #quant * 1.08 ?
print('\n')

