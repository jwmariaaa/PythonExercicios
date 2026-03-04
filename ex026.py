frase = str(input('Digite uma frase: ')).strip().upper()
print('A lestra A aparece {} vezes na frase'.format(frase.count('A')+1))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))