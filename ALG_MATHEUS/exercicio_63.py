import math as m

""" Criar um algoritmo que efetue o cálculo do salário líquido de um professor. Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS.
prog 1ea36
int na;
real vha, pd, td, sb, si;
imprima "\nhoras trabalhadas:
leia na
imprima "\nvaior da hora-aula:
leia vha
imprima "\npercentuai de desconto: H;
leia pd
sb <- na * vha;
td <- ( pd / 100) * sb;
501 s] <- sb — td;
imprima "\nsalario liquido: ",sl;
imprima U\flhl;  """

na = float(input('\n Horas trabalhadas: '))
vha = float(input('\n Valor da hora aula: '))
pd = float (input('\n Percentual de desconto: '))
sb = na*vha
td = (pd/100)*sb
sl = sb-td

print(f'\n Salario liquido: {sl}')
print('\n')
