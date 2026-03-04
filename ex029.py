velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tudo dentro do limite permitido!')
print('Tenha um bom dia! Dirija com segurança!')
