# Pintando uma parede#
print('Ola! Vamos Calcular a quantidade de tinta para pintar uma parede?')
larg = float(input('Me diga a Largura da parede: '))
alt = float(input('Agora me diga a Altura da parede: '))
area = larg * alt
print(
    f'Com base nos dados, sua parede tem uma dimensão de {larg}x{alt} dado isso, sua área é de {area}m².')
tinta = area / 2
print('__________________________________________________________________________________________________________')
print(
    f'Agora considerando que a cada 2m² gastam 1 litros de tinta,\nPara pintar sua parede você precisará de {tinta} litros de tinta.')
print(';)')
