conta = int(input('\n Digite conta de tres digitos:'))
d1 = int(conta/100)
d2 = int(conta%100/10)
d3 = int(conta%100%10)
inv = int(d3*100+d2*10+d1)
soma = int(conta+inv)
d1 = int((soma/100)*1)
d2 = int(soma%100/10)*2
d3 = int(soma%100%10)*3
digito = int(d1+d2+d3)%10

print(f'\n Digito verificador: {digito}')
print('\n')
