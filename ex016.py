from math import trunc
num = float(input('digite um valor: '))
print('o valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
# trunc transforma o número quebrado em inteiro, mas ao invés de usar ele, posso apenas usar o int nesse caso
