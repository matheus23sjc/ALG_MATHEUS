import math as a

lado = float(input('\n digite o lado do quadrado: '))
perimetro = (4*lado)
area = (lado**2)
diagonal = lado*a.sqrt(2)

print(f'\n perimetro: {perimetro}')
print(f'\n area: {area}')
print(f'\n diagonal: {diagonal:.2f}')
print('\n')

