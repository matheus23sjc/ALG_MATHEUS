import math as m 

""" Entrar com valores para xnum 1, xnum2 e xnum3 e imprimir o valor de x, sabendo-se que:
X = xnuml +
xnum2
+ 2(xnuml - xnum2) + 1 og 64
2
xnum3 + xnuml
48
prog lea3l
real xnuml, xnuni2, xnum3, x;
imprima "\nEntrar com 1 valor:
leia xnuml;
imprima "\nEntrar com 2 valor:
leia xnum2,
imprima "\nEntrar com 3 valor: hI
leia xnum3;
x <- xnuml + xnum2 / (xnum3 + xnuml) + 2 *(xnuml - xnum2) + log(64 )/
log(2 ),
imprima 11 \nX = x,
imprima " \n 11 ,  """

xnum1 = float(input('\n Entrar com 1 valor: '))
xnum2 = float(input('\n Entrar com 2 valor: '))
xnum3 = float(input('\n Entrar com 3 valor: '))
x = xnum1+xnum2/(xnum3+xnum1)+2*(xnum1-xnum2)+m.log(64.)/m.log(2.)

print(f'\n x: {x:.2f}')
print('\n')
