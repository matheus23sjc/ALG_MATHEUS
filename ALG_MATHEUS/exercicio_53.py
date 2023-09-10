import math as m

""" Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal.
prog 1ea26
real a, b, c, diagonal;
imprima "\nentre com a base: ;
leia a;
imprima "\nentre com a altura:
 1eia b;
imprima "\nentre com a profundidade:
leia c;
diagonal <-raiz( a**2 + b**2 + c**2 );
imprima "\ndiagonal : ", diagonal;
imprima "\n";  """

a = float(input('\n entre com a base: '))
b = float(input('\n entre com a altura: '))
c = float(input('\n entre com a profundidade: '))
diagonal = m.sqrt(a**2+b**2+c**2)

print(f'\n diagonal: {diagonal:.2f}')
print('\n')

