import math as m

""" Entrar com as notas da PR 1 e PR2 e imprimir a média final:
m truncada:
arredondada:
prog lea3O
real pri, pr2, mf;
imprima "\ndigite pri:
leia pri;
imprima "\ndigite pr2:
leia pr2;
mf <- ( pri + pr2 ) / 2;
imprima "\nmedia truncada = , realint((mf- 0.5)+0.001);
imprima "\nmedia arredondada = ", realint( mf+0.001);
imprima 11 \n";  """

pr1 = float(input('\n digite pr1: '))
pr2 = float(input('\n digite pr2: '))
mf = (pr1+pr2)/2

print(f'\n media truncada: {round((mf-0.5)+0.001)}')
print(f'\n media arredondada: {round(mf+0.001)}')
print('\n')