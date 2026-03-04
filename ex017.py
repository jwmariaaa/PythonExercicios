import math
co = float(input('digite o valor do cateto oposto '))
ca = float(input('digite o valor do cateto adjacente '))
hipotenusa = math.hypot(co, ca)
#ou (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hipotenusa))
