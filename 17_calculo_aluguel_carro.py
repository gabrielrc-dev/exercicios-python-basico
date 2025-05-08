# Aluguel de carros#
print("===== SISTEMA DE ALUGUEL DE VEÍCULOS =====")
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diaria = float(input('Qual o valor da diária cobrada? '))
kmrodado = float(input('Quantos estava cobrando por km rodado? '))
pago = (dias * diaria) + (km * kmrodado)
print(f'\n💰 O total a pagar é de R${pago:.2f}')
