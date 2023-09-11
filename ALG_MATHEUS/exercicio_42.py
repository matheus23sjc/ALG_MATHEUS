import math as m

angulo = float(input('Digite um angulo em graus: '))
rang = (angulo*3.14)/180

print(f'\n Seno: {m.sin(rang)}')
print(f'\n Co-seno: {m.cos(rang)}')
print(f'\n Tangente: {m.tan(rang)}')
print(f'\n Co-secante: {1/m.sin(rang)}')
print(f'\n Secante: {1/m.cos(rang)}')
print(f'\n Cotangente: {1/m.tan(rang)}')
print('\n')
