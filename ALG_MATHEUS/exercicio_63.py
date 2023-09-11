import math as m

na = float(input('\n Horas trabalhadas: '))
vha = float(input('\n Valor da hora aula: '))
pd = float (input('\n Percentual de desconto: '))
sb = na*vha
td = (pd/100)*sb
sl = sb-td

print(f'\n Salario liquido: {sl}')
print('\n')
