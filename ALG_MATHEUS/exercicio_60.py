import math as m

""" Entrar com a razão de uma PA e o valor do 1 2termo. Calcular imprimiro 10 termo da serie
prog 1ea33
int dec, razao, termo,
imprima "\nEntrar com o lo termo:
leia termo,
imprima "\nEntrar com a razao
leia razao,
dec <- termo + 9 razao,
imprima "\nO 10 termo desta P.A. e ", dec,
imprima " \n,  """

termo = int(input('\n Entrar com o 1° termo: '))
razao = int(input('\n Entrarcom a razao: '))
dec = termo+9*razao

print(f'\n O 10° termo desta P.A e: {dec}')
print('\n')
