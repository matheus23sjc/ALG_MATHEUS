import math as a

sm = float(input('\n entre com o salario minimo: '))
quantidade = float(input('\n entre com a quatidade em quilowatt: '))
preço = sm/700
vp = preço*quantidade
vd = vp*0.9

print(f'\n O preço do quilowatt: {preço} \n O valor a ser pago: {vp:.2f} \n O valor com desconto: {vd:.2f}')
print('\n')