# Conversor de Medidas#

medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print(f'A média de {medida} m corresponde a {dm} dm, {cm} cm e {mm} mm \nE também corresponde a {dam} dam, {hm} hm e {km} km ;)')
