import math as a

base = float(input('\ndigite base: '))
altura = float(input('\ndigite altura: '))
perimetro = 2*(base+altura)
area = base*altura
diagonal = a.sqrt(base**2+altura**2)

print(f'\n perimetro: {perimetro}')
print(f'\n area: {area}')
print(f'\n diagonal: {diagonal:.2f}')
print('\n')
