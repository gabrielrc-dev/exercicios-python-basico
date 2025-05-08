# Conversor de Moedas#

real = float(input('Digite o valor para converter: '))
dolar = real / 5.70
euro = real / 6.41
libra = real / 7.56
print(f'Com R${real} você pode comprar US$ {dolar:.2f}')
print(f'Com R${real} você pode comprar EUR {euro:.2f}')
print(f'Com R${real} você pode comprar LBR {libra:.2f}')
