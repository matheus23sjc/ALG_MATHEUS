import math as m

""" Criar um algoritmo que calcule e imprima a área de um losango.
prog 1ea28
real diagmaior, diagmenor, area;
imprima "\nmedida da diagonal maior:
leia diagmaior;
imprima "\nmedida da diagonal menor:
leia diagmenor;
area <- (diagmaior * diagmenor)/2;
imprima "\narea =", area;
imprima "\n";  """

diagmaior = float(input('\n medida do diagonal maior: '))
diagmenor = float(input('\n medida da diagonal menor: '))
area = (diagmaior*diagmenor)/2

print(f'\n area: {area}')
print('\n')
