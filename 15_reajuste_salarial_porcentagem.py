# Reajuste salarial, Porcentagem#
salario = float(input('Informe o salário do funcionário: R$'))
aumento = float(input('Informe quantos porcento que deseja aumentar: '))
novo = salario + (salario*aumento / 100)
print(
    f'Um funcionáriuo que ganhava R${salario:.2f}, com {aumento:.2f}% de aumento\nAgora passa a receber R${novo:.2f}\n;)')
