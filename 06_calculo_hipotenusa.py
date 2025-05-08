# Catetos e Hipotenusa com FORMATAÇÃO#

import math
co1 = float(input('Comprimento do cateto oposto: '))
ca1 = float(input('Comprimento do cateto adjacente: '))
hi1 = math.hypot(co1, ca1)
print(f'A hipotenusa vai medir: {hi1:.2f}')
