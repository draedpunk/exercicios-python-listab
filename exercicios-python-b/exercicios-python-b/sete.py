# Questão 7:
# Desenvolva um programa, em Python, que solicite ao usuário que insira um número
# inteiro. Com base no número fornecido, o programa determinará se ele é positivo,
# negativo ou zero.

numero = int(input("Informe um número inteiro --> "))

if (numero > 0):
    print("O numero é positivo.")
elif (numero < 0):
    print("O numero é menor que zero.")
else:
    print("O numero é igual a zero.")