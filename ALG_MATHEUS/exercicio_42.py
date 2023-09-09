import math as m
""" Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante,
co-secante e co-tangente deste ângulo.
prog leal5
real angulo, rang;
imprima "\ndigite um angulo em graus:
leia angulo;
rang <- ang u lo*pi 1180;
imprima "\nseno: ", sen(rang);
imprima \nco-seno: ", cos(rang);
imprima "\ntangente: ", tan(rang);
imprima "\nco-secante: ,1/ sen(rang);
imprima "\nsecante: ", 11cos(rang);
imprima "\ncotangente: ", 1/ tan(rang);
imprima "\n";  """

angulo = float(input('Digite um angulo em graus: '))
rang = (angulo*3.14)/180

print(f'\n Seno: {m.sin(rang)}')
print(f'\n Co-seno: {m.cos(rang)}')
print(f'\n Tangente: {m.tan(rang)}')
print(f'\n Co-secante: {1/m.sin(rang)}')
print(f'\n Secante: {1/m.cos(rang)}')
print(f'\n Cotangente: {1/m.tan(rang)}')
print('\n')
