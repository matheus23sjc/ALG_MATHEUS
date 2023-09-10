import math as a

""" Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
peri metro
area
diagonal:
prog 1ea23
real perimetro, area, diagonal, base, altura;
imprima "\ndigite base:
leia base,
imprima "\ndigite altura:
leia altura,
perimetro < 2*(base + altura);
area <-base * altura;
diagonal <- raiz(base**2 + alt u ra**2),
imprima "\nperimetro = " ,perimetro,
imprima "\narea = ", area , 45
imprima "\ndiagonal = ", diagonal
imprima "\n;  """

base = float(input('digite base: '))
altura = float(input('digite altura: '))
perimetro = 2*(base+altura)
area = base*altura
diagonal = a.sqrt(base**2+altura**2)

print(f'\n perimetro: {perimetro}')
print(f'\n area: {area}')
print(f'\n diagonal: {diagonal:.2f}')
print('\n')
