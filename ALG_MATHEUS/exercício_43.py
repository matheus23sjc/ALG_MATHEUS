import math as a

""" Entrar com um número e imprimir o logaritmo desse número na base 10.
prog leal6
1 real num, logaritmo;
imprima "\nentre com o logaritmando:
leia num;
logaritmo <- log(num) / log(10);
imprima "\nlogaritmo: ", logaritmo;
imprima "\n";  """

num = float(input('Entre com o logaritmando:'))
logaritmo = (a.log(num)/a.log(10))

print(f'\n Logaritmo: {logaritmo}')