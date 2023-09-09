""" Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.
prog leal7
real num, base, logaritmo;
imprima "\nentre com o logaritmando: ;
leia num;
imprima \nentre com a base: ";
leia base;
logaritmo <- log(num) / log(base);
imprima "\no logaritmo deb", num, "bna baseb",base, "be:b", logaritmo;
imprima "\n";
fi mprog  """

import math as a

num = float(input('Entre com o logaritmando: '))
base = float (input('Entre com a base: '))
logaritmo = (a.log(num)/a.log(base))

print(f'O logaritmo: {num} A base: {base} Logaritmo: {logaritmo:.2f}')
print('\n')