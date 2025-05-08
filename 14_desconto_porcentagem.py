# Desconto, Porcentagem#

produto = float(input('Olá, digite o valor do produto: R$ '))
desconto = float(
    input('Agora digite o valor do desconto qual será aplicado: '))
print('\n')
valorcomdesconto = produto * desconto / 100
valorfinal = produto - valorcomdesconto
print(f'Como o produto custa: R${produto:.2f}, e o desconto aplicado foi de: {desconto:.2f}%, o valor do desconto será: R${valorcomdesconto:.2f}\nE o valor final será de: R${valorfinal:.2f}')
print('\n;)')
