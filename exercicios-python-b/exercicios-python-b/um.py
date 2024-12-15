# QUESTÃO 1:
# Desenvolva um programa, em Python, que simule um sistema de compra de ingressos para um
# evento. O programa deverá permitir que o usuário compre ingressos, verificando se a
# quantidade solicitada está disponível no estoque. Caso a quantidade seja válida, o programa
# deverá confirmar a compra e exibir uma mensagem de confirmação juntamente com a
# quantidade de ingressos restantes. Caso contrário, deverá informar que a compra não pode ser
# realizada devido à falta de ingressos. O processo de compra pode ser repetido até que o usuário
# decida encerrar o programa.

ingressos = 200
print(f"\033[1;35m{'------------ Show do Montionless in White Brazil 2024 ------------':^35}\033[m")
print("Quantidade de ingressos disponível:", ingressos)

while (ingressos > 0): 
    try:
        qtd_ingresso = int(input("\nInforme a quantidade de ingressos que você deseja comprar: "))

        if (qtd_ingresso <= 0):
            print("\033[1;36m❌ Quantidade inválida!\033[m")
        elif (qtd_ingresso > ingressos):
            print("\033[1;36m❌ Quantidade inválida!\033[m")
        else:
            ingressos -= qtd_ingresso
            print("\n\033[1;32m✅ Compra realizada com sucesso!\033[m")
            print("Ingressos restantes:", ingressos)
    except ValueError:
        print("\033[1;36m❌ Entrada inválida!\033[m")
    
    opc = input("Você deseja comprar mais ingressos (S/N)? ").strip().lower()
    if (opc != 's'):
        print("\033[1;36m\nProgramada encerrado.\033[m")
        print("Aproveite o show! 🤘")
        break
else:
    print("\033[1;31mIngressos esgotados! Obrigado pelas compras.\033[m")

    
