import math as a

num = int(input('\nEntre com um numero e 3 digitos: '))
c = num//100
d = num%100//10
u = num%10
num1 = u*100+d*10+c

print(f'\n Número: {num}')
print(f'\n Invertido: {num1}')
print('\n')