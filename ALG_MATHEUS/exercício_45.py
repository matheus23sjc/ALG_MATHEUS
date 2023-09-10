""" Entrar com um número e imprimir a seguinte saída:
numero:
quadrado:
raiz quadrada:
prog leal8
real num, quad, raizquad;
imprima "\ndigite numero:
leia num;
quad <-num ** 2;
raizquad <- raiz(num);
imprima "\nnumero: ", num;
imprima "\nquadrado: ", quad;
imprima "\nraiz quadrada: ", raizquad;
imprima "\n";  """

import math as a

num = float(input('Digite numero: '))
quad = (num**2)
raizquad = (a.sqrt(num))

print(f'\n Numero: {num}')
print(f'\n Quadrado: {quad}')
print(f'\n Raiz quadrada: {raizquad}')
print('\n')
