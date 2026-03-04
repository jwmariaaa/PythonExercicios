km = float(input('qual a quantidade de km percorrido: '))
dias = int(input('qual a quantidade de dias percorrido: '))
preço = (60 * dias) + (0.15 * km)
print('O preço a pagar é de R${:.2f}'.format(preço))