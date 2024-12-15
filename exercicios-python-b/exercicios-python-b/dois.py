#Questão 2:
# Desenvolva um programa, em Python, que solicite ao usuário que insira a sua altura em
# centímetros. Com base na altura fornecida, o programa determinará se a pessoa é
# considerada baixa, média ou alta

altura = float(input("Informe o valor da sua altura (em cm)  --> "))

if (altura < 150):
    print("Você é considerado baixo.")

elif (150 <= altura < 180 ):
    print("Você tem uma altura média.")
else:
    print("Você é considerado alto.")