# Catetos e Hipotenusa sem FORMATAÇÃO#

co = float(input('Conprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir: {hi:.2f}')
