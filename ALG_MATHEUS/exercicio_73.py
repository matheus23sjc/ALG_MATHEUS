num = float(input('\n Entre com um numero com parte fracionaria: '))
numi = round((num-0.5))
numfrac = num-numi
numa = round(num+0.00001)

print(f'\n Parte inteira: {numi}')
print(f'\n Parte fracionaria: {numfrac+0.00001:.3f}')
print(f'\n Numero arredondado: {numa}')
print('\n')

