import math as m


pr1 = float(input('\n digite pr1: '))
pr2 = float(input('\n digite pr2: '))
mf = (pr1+pr2)/2

print(f'\n media truncada: {round((mf-0.5)+0.001)}')
print(f'\n media arredondada: {round(mf+0.001)}')
print('\n')