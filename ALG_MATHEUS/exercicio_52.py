import math as a

""" Entrar com o lado de um quadrado e imprimir:
peri metro:
area:
diagonal:
prog 1ea25
real lado, perimetro, area, diagonal;
imprima "\ndigite o lado do quadrado:
leia lado
perimetro <_ 4 * lado;
area<- lado ** 2;
diagonal <- lado * raiz(2);
imprima "\nperimetro: ", perimetro;
imprima "\narea: ", area;
imprima "\ndiagonal: ", diagonal;
imprima "\n"; 
 """
lado = float(input('\n digite o lado do quadrado: '))
perimetro = (4*lado)
area = (lado**2)
diagonal = lado*a.sqrt(2)

print(f'\n perimetro: {perimetro}')
print(f'\n area: {area}')
print(f'\n diagonal: {diagonal:.2f}')
print('\n')

